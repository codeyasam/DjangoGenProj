from django.contrib.auth.forms import AuthenticationForm
from django import forms

class LoginForm(AuthenticationForm):
	username = forms.CharField(label="Username",
		widget=forms.TexInput(attrs={'name': 'username'}))
	password = forms.CharField(label="Password",
		widget=forms.PasswordInput(attrs={'name': 'password'}))