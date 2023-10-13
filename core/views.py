from django.shortcuts import render, HttpResponse


def test_core_app(request):
    return render(request, "test.html")
