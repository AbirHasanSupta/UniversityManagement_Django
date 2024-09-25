from django.core.exceptions import ValidationError


def registration_validator(value):
    if len(str(value)) != 8:
        raise ValidationError("Registration Number must contain 8 digits")
