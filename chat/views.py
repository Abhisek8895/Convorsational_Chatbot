from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import ChatSession, ChatMessage
from .llm import generate_ai_response

from langchain_core.messages import HumanMessage, AIMessage

import uuid


@login_required
def chat_view(request, session_id = None):

    user = request.user
    # Start new chat
    if request.GET.get("new"):
        if "session_id" in request.session:
            del request.session["session_id"]

        return redirect("chat")
    if session_id:
        session = ChatSession.objects.get(
            user=user,
            session_id=session_id
        )
        request.session["session_id"] = session_id

    else:
        session_id = request.session.get("session_id")

        if not session_id:
            session_id = str(uuid.uuid4())
            request.session["session_id"] = session_id

            session = ChatSession.objects.create(
                user=user,
                session_id=session_id
            )
        else:
            session = ChatSession.objects.get(
                user=user,
                session_id=session_id
            )

    # Handle user message
    if request.method == "POST":

        user_message = request.POST.get("message")

        if user_message:

            # Save user message
            ChatMessage.objects.create(
                session=session,
                role="user",
                message=user_message
            )
            # Add sessio title
            if not session.title:
                max_length = 50
                session.title = user_message.strip()
                if len(session.title) > max_length:
                    session.title = session.title[:max_length-3] + "..."
                session.save()
            # Load chat history
            previous_messages = ChatMessage.objects.filter(
                session=session
            ).order_by("created_at")

            chat_history = []

            for msg in previous_messages:
                if msg.role == "user":
                    chat_history.append(
                        HumanMessage(content=msg.message)
                    )
                else:
                    chat_history.append(
                        AIMessage(content=msg.message)
                    )

            # Generate AI response using LLM
            ai_response = generate_ai_response(
                chat_history,
                user_message
            )

            # Save AI response
            ChatMessage.objects.create(
                session=session,
                role="ai",
                message=ai_response
            )

    # Fetch all messages for display
    messages = ChatMessage.objects.filter(
        session=session
    ).order_by("created_at")
    # Fetch all sessions for the sidebar
    conversations = ChatSession.objects.filter(
        user=user,
        chatmessage__isnull=False
    ).distinct().order_by("-created_at")

    return render(request, "chat.html", {"messages": messages,"conversations":conversations, "user":user})