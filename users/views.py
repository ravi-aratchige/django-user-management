from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from core import views


def sign_in(request):
    # form to render on login page (for context dictionary)
    form = LoginForm()

    # title to diplay on login page (for context dictionary)
    title = "Sign In"

    if request.method == "POST":
        # # create instance of LoginForm and populate it using data from POST request
        form = LoginForm(request.POST)

        if form.is_valid():
            # get submitted username and password
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            # authenticate user against users in database
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("/home/", {"username": username})

            else:
                messages.error(request, f"Could not find user {username} in system!")

    return render(request, "auth/sign-in.html", {"form": form})


def sign_up(request):
    # form to render on sign up page (for context dictionary)
    form = RegistrationForm()

    # title to diplay on sign up page (for context dictionary)
    title = "Create Account"

    # if user has pressed "Submit" on sign-up form:
    if request.method == "POST":
        # create instance of RegistrationForm and populate it using data from POST request
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # automatically log in the new user
            login(request, user)

            # redirect to the home page, with the new user in the context
            return redirect("/home/", {"username": request.user.username})

    return render(request, "auth/sign-up.html", {"form": form})


def sign_out(request):
    logout(request)
    return redirect("/")


def delete_account(request):
    if request.user.is_authenticated:
        user = request.user
        user.delete()
        logout(request)
        return redirect("/")
