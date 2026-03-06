from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    else:
        form = SignupForm()

    return render(request, "signup.html", {"form": form})



def login_view(request):

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")

    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})


@login_required
def home(request):
    return render(request, "home.html")

def landing_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    return render(request, "landing.html")

def logout_view(request):
    logout(request)
    return redirect("landing")