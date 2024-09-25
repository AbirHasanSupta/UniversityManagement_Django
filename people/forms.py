from django import forms
from .models import Teachers, Students
from .form_validation import registration_validator

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teachers
        fields = "__all__"

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = "__all__"

        widgets = {
            "date_of_birth" : forms.DateInput(attrs={
                "type" : "date"
            }),
            "registration_id" : forms.TextInput(attrs={
                "maxlength": 8,
            })
        }
    def cleaned_registration_id(self):
        registration_id = self.cleaned_data["registration_id"]
        registration_validator(registration_id)
        return registration_id
