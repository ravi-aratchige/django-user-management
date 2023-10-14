from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, "home.html")


def test_core_app(request):
    return render(request, "test.html")
