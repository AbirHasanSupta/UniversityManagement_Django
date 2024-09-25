from django.urls import path

from . import views

urlpatterns = [
    path("students/", views.add_student, name="add_student"),
    path("students/edit/<int:pk>", views.edit_student, name="edit_student"),
    path("students/delete/<int:pk>", views.delete_student, name="delete_student"),
    path("students/delete/all", views.delete_all_student, name="delete_all_students"),
    path("students/add-course/<int:pk>", views.add_course, name="add_course")
]