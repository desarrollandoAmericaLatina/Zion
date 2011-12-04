# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from robame.forms import formUser, LoginForm
from robame.models import Usuario
from django.template import RequestContext
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def registroUser(request):
	if request.method == 'POST':
		form = formUser(request.POST)
		if form.is_valid():
			formSave = form.save()
			usuario = form.cleaned_data['username']
			correo = form.cleaned_data['email']
			mensaje = 'Su cuenta está activa. Puede ingresar al servicio con el usuario. '+str(usuario)+'. Gracias, por usar el servicio.'
			#send_mail('Creación de cuenta - roba.me', mensaje, 'no-reply@robame.pe', [correo], fail_silently=False)
			return render_to_response('inscripcion.html', {'formValido': True})
		else:
			context = {'form': form, 'formValido': False}
	else:
		form = formUser()
		context = {'form': form, 'formValido': False}
	return render_to_response('inscripcion.html', context, context_instance=RequestContext(request))
