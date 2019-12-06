from django import forms
from phonenumber_field.modelfields import *

from .models import Phonebook

class PhoneForm(forms.ModelForm):
    #name = forms.CharField(label='Name', max_length = 100, required=False)
    #phone_number = forms.CharField(label='Phone Number', max_length=10, required=False)

    class Meta:
        model = Phonebook
        fields='__all__'