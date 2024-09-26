from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Students, Teachers
from .tasks import send_email_task


@receiver(post_save, sender=Teachers)
@receiver(post_save, sender=Students)
def send_email_signal(sender, created, instance, **kwargs):
    if created:
        send_email_task.delay(instance.email, instance.name, instance.raw_password)
