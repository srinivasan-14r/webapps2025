from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# class RegisterForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#
#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))