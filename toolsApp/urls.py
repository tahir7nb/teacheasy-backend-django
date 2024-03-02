from django.urls import path
from . import views

urlpatterns = [
    path("verify_session_token", views.verify_session_token),
    path("get_lesson_planner_response", views.get_lesson_planner_response),
]
