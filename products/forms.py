from django import forms
from .models import Product

class ContactForm(forms.Form):
    fullname = forms.CharField()
    email    = forms.EmailField()
    content  = forms.CharField()


class stkForm(forms.Form):
    phonenumber = forms.CharField()
    price = forms.DecimalField()
