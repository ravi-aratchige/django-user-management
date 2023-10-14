"""
This module contains URL configurations for the 'core' app
of this project.
"""

from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.index, name="home"),
    path("test-core-app/", views.test_core_app, name="test-core-app"),
]
