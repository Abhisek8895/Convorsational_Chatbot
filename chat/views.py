from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ChatSession, ChatMessage
import uuid

@login_required
def chat_view(request):
    user = request.user

    # Create or get session id
    session_id = request.session.get('id')
    if not session_id:
        session_id = str(uuid.uuid4())  # generate unique session_id
        request.session['session_id'] = session_id
        session = ChatSession.objects.create(user=user, session_id=session_id)
    else:
        session = ChatSession.objects.get(user = user, session_id=session_id)

    # Save messages 
    if request.method == 'POST':
        user_message = request.POST.get('message')
        if user_message:
            ChatMessage.objects.create(session = session, role= 'user', message = user_message)

            ai_response = "Hi, I am currently getting build. Please wait until I am finished...😀"
            ChatMessage.objects.create(session = session, role= 'ai', message = ai_response)
    
    # Fetch all the messages
    messages = ChatMessage.objects.filter(session = session).order_by('created_at')

    return render(request, 'chat.html', {'messages': messages})