from django.db import models
from django.contrib.auth.models import User
from .choices import VALIDITY_CHOICES, TRANS_CHOICES


# Create your models here.

class Transaction(models.Model):
    User = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    Stock = models.CharField(max_length=200)

    Date = models.DateTimeField()

    Type = models.CharField(max_length=4, choices=TRANS_CHOICES)

    Regular = models.BooleanField(default=False, null=True, blank=True)
    CO = models.BooleanField(default=False, null=True, blank=True)
    BO = models.BooleanField(default=False, null=True, blank=True)
    AMO = models.BooleanField(default=False, null=True, blank=True)
    InterDay = models.BooleanField(default=False, null=True, blank=True)
    CNC = models.BooleanField(default=False, null=True, blank=True)
    Margin = models.BooleanField(default=False, null=True, blank=True)

    Market = models.BooleanField(default=False, null=True, blank=True)
    Limit = models.BooleanField(default=False, null=True, blank=True)
    Stop = models.BooleanField(default=False, null=True, blank=True)
    StopLimit = models.BooleanField(default=False, null=True, blank=True)

    Validity = models.CharField(max_length=3, choices=VALIDITY_CHOICES)

    Price = models.BooleanField(default=True)

    LimitPrice = models.FloatField()
    StopPrice = models.FloatField()
    StopLoss = models.FloatField()
    TakeProfit = models.FloatField()
    TrailingStopLoss = models.FloatField()

    Quantity = models.PositiveIntegerField()
    DisclosedQuantity = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False, blank=True)

    def __str__(self):
        return f'{self.User} {self.Stock} {self.Type} {self.Date}'

    class Meta:
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'


class UserList(models.Model):
    Creater = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User_id')

    Users = models.ManyToManyField(User)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return f'{self.Creater} {self.Users.all().values("username")}'

    class Meta:
        verbose_name = 'User List'
        verbose_name_plural = 'User Lists'


class Bucket(models.Model):
    Creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User')

    Users = models.ManyToManyField(User)

    created_at = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False, blank=True)

    def __str__(self):
        return f'{self.Creator} {self.Users.all().values("username")}'

    class Meta:
        verbose_name = 'Bucket'
        verbose_name_plural = 'Buckets'
