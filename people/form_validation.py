from django.core.exceptions import ValidationError


def registration_validator(value):
    if len(str(value)) < 8 < len(str(value)):
        raise ValidationError("Registration Number must contain 8 digits")
