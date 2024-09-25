from django.urls import path
from . import views

urlpatterns = [
    path("students/", views.add_student, name="add_student")
]