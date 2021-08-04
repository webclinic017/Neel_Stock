from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from .choices import VALIDITY_CHOICES, TRANS_CHOICES, BROKER_CHOICES
from phonenumber_field.modelfields import PhoneNumberField


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
    Creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User_id')

    Name = models.CharField(max_length=128, default=' ')                #
    Broker = models.CharField(max_length=15, choices=BROKER_CHOICES)    #
    UserId = models.CharField(max_length=128)                           #

    Password = models.CharField(max_length=256)                         #
    Email = models.EmailField()                                         #
    Phone = PhoneNumberField()                                          #

    Pin_2FA = models.CharField(max_length=128)                          #

    API_Key = models.CharField(max_length=256)                          #
    API_Secret = models.CharField(max_length=256)
    SubWebHook = models.CharField(max_length=256)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return f'{self.Name}'

    def delete_object(self):
        return reverse('core:delete_userlist', args=[str(self.id)])

    class Meta:
        verbose_name = 'User List'
        verbose_name_plural = 'User Lists'


class Bucket(models.Model):
    Creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User')
    Users = models.ManyToManyField(UserList)

    ActivateCopyTrade = models.BooleanField(default=False)
    Multiplier = models.PositiveIntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False, blank=True)

    def __str__(self):
        return f'{self.Creator} {self.Users.all()} {self.Multiplier}'

    def delete_object(self):
        return reverse('core:delete_bucket', args=[str(self.id)])

    class Meta:
        verbose_name = 'Bucket'
        verbose_name_plural = 'Buckets'


class WatchList(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)

    Stock = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False, blank=True)

    def __str__(self):
        return f'{self.User} {self.Stock}'

    def delete_object(self):
        return reverse('core:delete_watchlist', args=[str(self.id)])

    class Meta:
        verbose_name = 'WatchList'
        verbose_name_plural = 'WatchLists'


class Stock(models.Model):
    token = models.CharField(max_length=20)
    symbol = models.CharField(max_length=30)
    name = models.CharField(max_length=30)

    expiry = models.CharField(max_length=30)
    strike = models.CharField(max_length=30)
    lotsize = models.CharField(max_length=30)

    instrumenttype = models.CharField(max_length=30)
    exch_seg = models.CharField(max_length=30)

    tick_size = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Stock'
        verbose_name_plural = 'Stock'
