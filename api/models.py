from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from string import Template


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=True)

    phone_number = models.CharField(max_length=14, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return Template(f'{self.user.username}').template


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
