from django.urls import path

from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("login/", views.login_user, name="login"),
    path("register/", views.register_user, name="register"),
    path("logout/", views.logout_user, name="logout"),
    path("departments/", views.create_department, name="create_department"),
    path("departments/edit/<int:pk>", views.edit_department, name="edit_department"),
    path("departments/delete/<int:pk>", views.delete_department, name="delete_department"),
    path("departments/delete/all", views.delete_all_department, name="delete_all_departments"),
    path("courses/", views.create_course, name="create_course"),
    path("courses/edit/<int:pk>", views.edit_course, name="edit_course"),
    path("courses/delete/<int:pk>", views.delete_course, name="delete_course"),
    path("courses/delete/all", views.delete_all_course, name="delete_all_course")
]