from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login
from core import views


def sign_in(request):
    # form to render on login page (for context dictionary)
    form = LoginForm()

    if request.method == "POST":
        # # create instance of LoginForm and populate it using data from POST request
        form = LoginForm(request.POST)
        # username = request.POST["username"]
        # password = request.POST["password"]
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        if form.is_valid():
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, "home.html", {"username": user.get_username()})

    return render(request, "auth/sign-in.html", {"form": form})


def sign_up(request):
    # form to render on login page (for context dictionary)
    form = RegistrationForm()

    # if user has pressed "Submit" on sign-up form:
    if request.method == "POST":
        # create instance of RegistrationForm and populate it using data from POST request
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # return render(request, "home.html", {"username": request.username})
            login(request, user)
            return redirect("/home/", {"username": request.user.username})

    return render(request, "auth/sign-up.html", {"form": form})


def sign_out(request):
    pass
