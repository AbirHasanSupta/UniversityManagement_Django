from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_email_task(instance_email, instance_name, instance_password):
    subject = "Your Account Details"
    message = f"Dear {instance_name}, \n\nYour account has been created successfully.\nYour login details are:\n\nEmail: {instance_email}\nPassword: {instance_password}\n\nPlease keep this information safe."
    send_mail(subject, message, settings.EMAIL_HOST_USER, [instance_email])