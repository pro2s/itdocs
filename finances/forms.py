from django import forms
from django.forms import ModelForm
from finances.models import Payment

class PaymentForm(ModelForm):
        class Meta:
            model = Payment
