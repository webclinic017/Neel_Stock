from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from .choices import VALIDITY_CHOICES, TRANS_CHOICES, BROKER_CHOICES, PRODUCT_TYPE_CHOICES, ADV_PRODUCT_TYPE, ORDER_TYPE_CHOICES
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.


class Bucket(models.Model):
    Creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Bucket_Creator')
    Users = models.ManyToManyField(User, through='Multiplier')

    ActivateCopyTrade = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False, blank=True)

    def __str__(self):
        users_query = self.Users.all()
        users_str = ''
        for user in users_query:
            users_str = users_str + user.username + ', '
        return f'{self.Creator} / {users_str} '

    def delete_object(self):
        return reverse('core:delete_bucket', args=[str(self.id)])

    class Meta:
        verbose_name = 'Bucket'
        verbose_name_plural = 'Buckets'


class Multiplier(models.Model):
    Bucket = models.ForeignKey(Bucket, on_delete=models.CASCADE)
    User = models.ForeignKey(User, on_delete=models.CASCADE)

    multiplier = models.PositiveIntegerField(default=1)


class Transaction(models.Model):
    User = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    Stock = models.CharField(max_length=200)
    Bucket = models.ForeignKey(Bucket, on_delete=models.PROTECT, null=True)

    Date = models.DateTimeField()

    Type = models.CharField(max_length=4, choices=TRANS_CHOICES)

    ProductType = models.CharField(max_length=7, choices=PRODUCT_TYPE_CHOICES, default='Regular')

    AdvanceProductType = models.CharField(max_length=8, choices=ADV_PRODUCT_TYPE, default='Intraday')

    OrderType = models.CharField(max_length=10, choices=ORDER_TYPE_CHOICES, default='Market')

    Validity = models.CharField(max_length=3, choices=VALIDITY_CHOICES, default='Day')

    Price = models.BooleanField(default=True)

    LimitPrice = models.FloatField(null=True, blank=True)
    StopPrice = models.FloatField(null=True, blank=True)
    StopLoss = models.FloatField(null=True, blank=True)
    TakeProfit = models.FloatField(null=True, blank=True)
    TrailingStopLoss = models.FloatField(null=True, blank=True)

    Quantity = models.PositiveIntegerField(null=True, blank=True)
    DisclosedQuantity = models.PositiveIntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False, blank=True)

    def __str__(self):
        return f'{self.User} {self.Stock} {self.Type} {self.Date}'

    class Meta:
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'


class WatchList(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)

    Stocktoken = models.CharField(max_length=200, null=True)
    Stocksymbol = models.CharField(max_length=200, null=True)
    Stockname = models.CharField(max_length=200, null=True)
    Stockexch_seg = models.CharField(max_length=200, null=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False, blank=True)

    def __str__(self):
        return f'{self.User} {self.Stocktoken}'

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
