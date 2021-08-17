from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

from core.choices import BROKER_CHOICES


# Create your models here.

class Profile(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    Broker = models.CharField(max_length=15, choices=BROKER_CHOICES, null=True, blank=True)  #
    UserId = models.CharField(max_length=128, null=True, blank=True)  #

    Password = models.CharField(max_length=256, null=True, blank=True)  #

    Pin_2FA = models.CharField(max_length=128, null=True, blank=True)  #

    API_Key = models.CharField(max_length=256, null=True, blank=True)  #
    API_Secret = models.CharField(max_length=256, null=True, blank=True)
    SubWebHook = models.CharField(max_length=256, null=True, blank=True)

    PhoneNumber = PhoneNumberField(null=True, blank=True)

    account_manager = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'


    def __str__(self):
        return f'{self.User} {self.PhoneNumber}'
