from django import forms
from .models import *


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'image', 'description']


class CheckoutForm(forms.Form):
    total_amount = forms.DecimalField(max_digits=10, decimal_places=2)
    barcode = forms.CharField(max_length=100)
    delivery_info = forms.CharField(widget=forms.Textarea)
