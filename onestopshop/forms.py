from django import forms

from .models import OneStopShop


class OneStopShopForm(forms.ModelForm):
    class Meta:
        model = OneStopShop
        fields = '__all__'
