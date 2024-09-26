from django.urls import path
from . import views

urlpatterns = [
    path("students/", views.add_student, name="add_student"),
    path("students/edit/<int:pk>", views.edit_student, name="edit_student"),
    path("students/delete/<int:pk>", views.delete_student, name="delete_student"),
    path("students/delete/all", views.delete_all_student, name="delete_all_students"),
    path("students/add-course/<int:pk>", views.add_course, name="add_course"),
    path("teachers/", views.add_teacher, name="add_teacher"),
    path("teachers/edit/<int:pk>", views.edit_teacher, name="edit_teacher"),
    path("teachers/delete/<int:pk>", views.delete_teacher, name="delete_teacher"),
    path("teachers/delete/all", views.delete_all_teacher, name="delete_all_teachers"),
    path("teachers/add-course/<int:pk>", views.add_teacher_course, name="add_teacher_course"),
    path("teachers/course/<int:pk>/students/", views.student_list, name="student_list")
]