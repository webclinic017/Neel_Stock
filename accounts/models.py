from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)

    PhoneNumber = PhoneNumberField()

    def __str__(self):
        return f'{self.User} {self.PhoneNumber}'

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
