from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models  import *

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='login', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username','password')

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'context': forms.Textarea(attrs={'class': 'form-control', 'rows':5}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }