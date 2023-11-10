from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User 
from django import forms
from . models import Client


class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username' , 'password1' , 'password2']



class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput())
    password=forms.CharField(widget=forms.PasswordInput())



class AddClient(forms.ModelForm):
    class Meta:
        model=Client
        fields='__all__'

class UpdateClient(forms.ModelForm):
    class Meta:
        model=Client
        fields='__all__'




