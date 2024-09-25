from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from university.models import Courses
from .models import Teachers, Students
from .forms import TeacherForm, StudentForm, StudentAddCourseForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url="login")
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
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