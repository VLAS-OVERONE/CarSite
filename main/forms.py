from  .models import Vehicle
from django.forms import ModelForm, TextInput, Textarea
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = ["title", "description"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название автомобиля',
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание автомобиля'
            }),
        }