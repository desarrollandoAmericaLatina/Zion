# -*- coding: utf-8 -*-
from django import forms
from django.db import models
from robame.models import Asalto
from robame.models import Usuario

class AsaltoForm(forms.ModelForm):
	class Meta:
		model = Asalto
		exclude = ['fecha', 'hora']
		
class formUser(forms.ModelForm):
	username = forms.CharField(label = 'Nombre de usuario', max_length=50)
	password = forms.CharField(label = 'Contraseña', widget=forms.PasswordInput)
	email = forms.EmailField(label= 'Correo electrónico', max_length="100")
	class Meta:
		model = Usuario
		exclude = ['first_name', 'last_name', 'is_staff', 'is_active', 'groups', 'last_login', 'date_joined', 'is_superuser', 'user_permissions']

class LoginForm(forms.Form):
	username = forms.CharField(label = "Nombre de usuario", max_length=50)
	passwd = forms.CharField(label="Contraseña", widget = forms.PasswordInput)
