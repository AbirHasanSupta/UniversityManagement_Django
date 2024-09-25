from django import forms
from .models import Teachers, Students
from university.models import Courses
from .form_validation import registration_validator

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teachers
        fields = "__all__"

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        exclude = ["course"]

        widgets = {
            "date_of_birth" : forms.DateInput(attrs={
                "type" : "date"
            }),
            "registration_id" : forms.TextInput(attrs={
                "maxlength": 8,
            })
        }

    def clean_registration_id(self):
        registration_id = self.cleaned_data["registration_id"]
        registration_validator(registration_id)
        return registration_id

class StudentAddCourseForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ["course"]

    def __init__(self, *args, **kwargs):
        student = kwargs.get("instance")
        super(StudentAddCourseForm, self).__init__(*args, **kwargs)
        if student:
            self.fields["course"].queryset = Courses.objects.filter(department=student.department)
