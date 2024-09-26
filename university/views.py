from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Departments, Courses
from .forms import DepartmentForm, CourseForm
from django.contrib import messages
from django.contrib.auth import login, logout


def dashboard(request):
    return render(request, "dashboard.html")


def login_user(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    if request.method == "POST":
        form =  AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Please insert correct credentials")
    form = AuthenticationForm()
    return render(request, "login.html", {"form" : form})


def register_user(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            messages.success(request, "Registration Successful")
            return redirect("login")
        else:
            messages.error(request, form.errors)
    form = UserCreationForm()
    return render(request, "register.html", {"form" : form})


def logout_user(request):
    logout(request)
    return redirect("login")


def create_department(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("create_department")
    form = DepartmentForm()
    return render(request, "departments.html", {"form": form})


def edit_department(request, pk):
    department = Departments.objects.get(pk=pk)
    if request.method == "POST":
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect("create_department")
    form = DepartmentForm(instance=department)
    return render(request, "departments.html", {"form" : form})


def delete_department(request, pk):
    department = Departments.objects.get(pk=pk)
    department.delete()
    return redirect("create_department")


def delete_all_department(request):
    if request.method == "POST":
        departments = Departments.objects.all()
        departments.delete()
        return redirect("create_department")
    return render(request, "delete_all_departments.html")


def create_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("create_course")
    form = CourseForm()
    return render(request, "courses.html", {"form": form})


def edit_course(request, pk):
    courses = Courses.objects.get(pk=pk)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=courses)
        if form.is_valid():
            form.save()
            return redirect("create_course")
    form = CourseForm(instance=courses)
    return render(request, "courses.html", {"form": form})


def delete_course(request, pk):
    course = Courses.objects.get(pk=pk)
    course.delete()
    return redirect("create_course")


def delete_all_course(request):
    if request.method == "POST":
        courses = Courses.objects.all()
        courses.delete()
        return redirect("create_course")
    return render(request, "delete_all_courses.html")