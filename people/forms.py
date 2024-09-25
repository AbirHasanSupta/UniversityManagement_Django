from django import forms
from .models import Teachers, Students


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teachers
        fields = "__all__"

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = "__all__"