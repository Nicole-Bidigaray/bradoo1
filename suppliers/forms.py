from django.forms import ModelForm
from django import forms
from .models import Provider, Product


class ProviderForm(ModelForm):
    class Meta:
        model = Provider
        fields = '__all__'


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
