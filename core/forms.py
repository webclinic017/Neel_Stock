from django import forms
from .models import WatchList, Stock, Transaction, Bucket


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
            'Price': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'LimitPrice': forms.NumberInput(attrs={'class': 'form-control'}),
            'StopPrice': forms.NumberInput(attrs={'class': 'form-control'}),
            'StopLoss': forms.NumberInput(attrs={'class': 'form-control'}),
            'TakeProfit': forms.NumberInput(attrs={'class': 'form-control'}),
            'TrailingStopLoss': forms.NumberInput(attrs={'class': 'form-control'}),
            'Quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'DisclosedQuantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }
