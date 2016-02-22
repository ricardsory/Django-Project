from django import forms

# Create your views here.

class Login(forms.Form):
    inputEmail = forms.CharField(label='Email', max_length=100)