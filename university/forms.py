from .models import Departments, Courses
from django import forms


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Departments
        fields = "__all__"


class CourseForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = "__all__"

