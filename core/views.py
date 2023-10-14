from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, "index.html")


def home(request):
    return render(request, "home.html")


def test_core_app(request):
    view_name = test_core_app.__name__
    return render(request, "test/test.html", {"view": view_name})
