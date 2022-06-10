from django import forms
from django.forms import ModelForm
from .models import Food, Shop

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class TextAreaInput(forms.Textarea):
    input_type = 'textarea'

class FoodForm(ModelForm):

    class Meta:
        model = Food
        widgets = {
            'created_at': DateTimeInput,
            'updated_at': DateTimeInput,
        }
        fields = [
            'title',
            'desc',
            'category',
            'shop'
        ]

class ShopForm(ModelForm):

    class Meta:
        model = Shop
        fields = [
            'name'
        ]
