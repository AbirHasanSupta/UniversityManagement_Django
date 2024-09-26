from django.dispatch import receiver
from django.db.models.signals import post_save

from UniversityManagement.settings import EMAIL_HOST_USER
from .models import Students
from django.core.mail import send_mail


@receiver(post_save, sender=Students)
def send_email_signal(sender, created, instance, **kwargs):
    if created:
        subject = "Your Account Details"
        message = f"Dear {instance.name}, \n\nYour account has been created successfully.\nYour login details are:\n\nEmail: {instance.email}\nPassword: {instance.raw_password}\n\nPlease keep this information safe."
        print(EMAIL_HOST_USER, instance.email)
        send_mail(subject,message, EMAIL_HOST_USER, [instance.email])
