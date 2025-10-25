from rest_framework import routers
from django.urls import path, include

from . import views


urlpatterns = [
    path("hello/", views.HelloView.as_view()),
]

app_name = "main"
