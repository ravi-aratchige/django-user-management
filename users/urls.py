from django.urls import path
from . import views

urlpatterns = [
    path("sign-in/", views.sign_in, name="sign-in"),
    path("sign-up/", views.sign_up, name="sign-up"),
    path("delete/", views.delete_account, name="delete-account"),
    path("sign-out/", views.sign_out, name="sign-out"),
]
