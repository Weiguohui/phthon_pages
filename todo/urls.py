# todo/urls.py
from django.urls import path

from .views import TodoPageView

urlpatterns = [
    path('todo/', TodoPageView, name='todolist'),
]
