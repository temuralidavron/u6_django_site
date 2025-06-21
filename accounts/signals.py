from django.core.mail import send_mail
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from accounts.models import CustomUser
from config import settings


@receiver(pre_save,sender=CustomUser)
def username_ustudy(sender,instance,**kwargs):
    if instance:
        instance.username += f"{instance.username} USTUDY"
        print(instance.username)


@receiver(post_save,sender=CustomUser)
def create_profile(sender,instance,created,**kwargs):
    if created:

        send_mail(

            subject="Bugun bayram",

            message="Wellcome ",

            from_email=settings.EMAIL_HOST_USER,

            recipient_list=[instance.email,],

            fail_silently=False,

        )

