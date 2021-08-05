from django import forms
from .models import UserList, Bucket, WatchList, Transaction, Stock


class UserForm(forms.ModelForm):

    class Meta:
        model = UserList
        exclude = ('Creator', 'created_at', 'updated_at')
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Broker': forms.Select(attrs={'class': 'form-control'}),
            'UserId': forms.TextInput(attrs={'class': 'form-control'}),
            'Password': forms.TextInput(attrs={'class': 'form-control'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control'}),
            'Phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+91 111 1234567', 'type': 'tel'}),
            'Pin_2FA': forms.TextInput(attrs={'class': 'form-control'}),
            'API_Key': forms.TextInput(attrs={'class': 'form-control'}),
            'API_Secret': forms.TextInput(attrs={'class': 'form-control'}),
            'SubWebHook': forms.TextInput(attrs={'class': 'form-control'}),
        }

        # def __init__(self, *args, **kwargs):
        #     super(UserForm, self).


class BucketForm(forms.ModelForm):
    class Meta:
        model = Bucket
        exclude = ('Creator', 'created_at', 'updated_at')
        widgets = {
            'Users': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'ActivateCopyTrade': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'Multiplier': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        exclude = ('User', 'created_at', 'updated_at', 'Date')
        widgets = {
            'Stock': forms.TextInput(attrs={'class': 'form-control'}),
            'Type': forms.Select(attrs={'class': 'form-control'}),
            'Regular': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'CO': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'BO': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'AMO': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'InterDay': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'CNC': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'Margin': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'Market': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'Limit': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'Stop': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'StopLimit': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'ValidityDay': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'ValidityIOC': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'Price': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'LimitPrice': forms.NumberInput(attrs={'class': 'form-control'}),
            'StopPrice': forms.NumberInput(attrs={'class': 'form-control'}),
            'StopLoss': forms.NumberInput(attrs={'class': 'form-control'}),
            'TakeProfit': forms.NumberInput(attrs={'class': 'form-control'}),
            'TrailingStopLoss': forms.NumberInput(attrs={'class': 'form-control'}),
            'Quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'DisclosedQuantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'Bucket': forms.Select(attrs={'class': 'form-control'}),
        }

