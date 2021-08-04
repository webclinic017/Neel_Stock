from django import forms
from .models import UserList, Bucket, WatchList, Transaction
from phonenumber_field.formfields import PhoneNumberField


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
