from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from university.models import Courses
from .models import Teachers, Students
from .forms import TeacherForm, StudentForm, StudentAddCourseForm, TeacherAddCourseForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from .password_generator import random_password_generator


@login_required(login_url="login")
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            raw_password = random_password_generator()
            hashed_password = make_password(raw_password)
            student.password = hashed_password
            student.raw_password = raw_password
            student.save()
            return redirect("add_student")
        else:
            messages.error(request, form.errors)
    form = StudentForm()
    return render(request, "people/students.html", {"form": form})

@login_required(login_url="login")
def edit_student(request, pk):
    student = Students.objects.get(pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("add_student")
    form = StudentForm(instance=student)
    return render(request, "people/students.html", {"form": form})
@login_required(login_url="login")
def add_course(request, pk):
    student = Students.objects.get(pk=pk)
    if request.method == "POST":
        form = StudentAddCourseForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
    form = StudentAddCourseForm(instance=student)
    return render(request, "people/add_course.html", {"form": form, "student": student})


@login_required(login_url="login")
def delete_student(request, pk):
    student = Students.objects.get(pk=pk)
    student.delete()
    return redirect("add_student")

@login_required(login_url="login")
def delete_all_student(request):
    if request.method == "POST":
        students = Students.objects.all()
        students.delete()
        return redirect("add_student")
    return render(request, "people/delete_all_students.html")


@login_required(login_url="login")
def add_teacher(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            teacher = form.save(commit=False)
            raw_password = random_password_generator()
            hashed_password = make_password(raw_password)
            teacher.password = hashed_password
            teacher.raw_password = raw_password
            teacher.save()
            return redirect("add_teacher")
        else:
            messages.error(request, form.errors)
    form = TeacherForm()
    return render(request, "people/teachers.html", {"form": form})

@login_required(login_url="login")
def edit_teacher(request, pk):
    teacher = Teachers.objects.get(pk=pk)
    if request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect("add_teacher")
    form = TeacherForm(instance=teacher)
    return render(request, "people/teachers.html", {"form": form})


@login_required(login_url="login")
def add_teacher_course(request, pk):
    teacher = Teachers.objects.get(pk=pk)
    if request.method == "POST":
        form = TeacherAddCourseForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
    form = TeacherAddCourseForm(instance=teacher)
    return render(request, "people/add_teacher_course.html", {"form": form, "teacher": teacher})


@login_required(login_url="login")
def delete_teacher(request, pk):
    teacher = Teachers.objects.get(pk=pk)
    teacher.delete()
    return redirect("add_teacher")

@login_required(login_url="login")
def delete_all_teacher(request):
    if request.method == "POST":
        teachers = Teachers.objects.all()
        teachers.delete()
        return redirect("add_teacher")
    return render(request, "people/delete_all_teachers.html")