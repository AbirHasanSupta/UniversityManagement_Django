from .models import Departments, Courses, Students, Teachers
from django import forms


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Departments
        fields = "__all__"


class CourseForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = "__all__"

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teachers
        fields = "__all__"

class StudentForm(forms.ModelForm):
    class Meta:
        models = Students
        fields = "__all__"