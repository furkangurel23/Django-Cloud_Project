from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import tbl_user

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	phone = forms.CharField(max_length=12)

	class Meta:
		model = User
		fields = ['username', 'email', 'phone', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = tbl_user
		fields = ['image']
		
