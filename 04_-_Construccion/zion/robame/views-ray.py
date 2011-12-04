# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from robame.forms import *
from robame.models import *
from django.template import RequestContext
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

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

def index_tmp(request):
	user = request.user
	if user is not None and user.is_active:
		isLogin = True
	else:
		isLogin = False
	print "Z"
	form = AsaltoForm()
	if request.method == 'POST':
		asaltoForm = AsaltoForm(request.POST)
		if asaltoForm.is_valid():
			descripcion_ = asaltoForm.cleaned_data['descripcion']
			asaltoForm.save()
			asalto = Asalto.objects.order_by('-id')[:1]
			saveTags(descripcion_, asalto[0].id)
			print "Zlll"
			return HttpResponseRedirect('/')
		else:
			print "Z"
			context = {'asaltoForm': asaltoForm,'isLogin':isLogin,'loginForm':LoginForm(), 'envioValido': False}
			return render_to_response('index.html',context)
	else:
		print "Z<"
		comentarios = getComentarios()
		if comentarios.count >= 3:
			comentarios = comentarios[:3]
		context = {'asaltoForm': form, 'envioValido': True,'isLogin':isLogin,'loginForm':LoginForm(), 'comentarios': comentarios}
		return render_to_response('index.html',context)

def getComentarios():
	comentarios = []
	for asalto in Asalto.objects.order_by('-fecha', '-hora'):		
		comentarios.append({'fecha':asalto.fecha, 'hora':asalto.hora, 'descripcion': asalto.descripcion, 'ciudad': getCiudad(asalto.latitud, asalto.longitud)})
	return comentarios

def loginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            passwd= form.cleaned_data['password']
            user = authenticate(username=username, password=passwd)
            if user is not None:
                if user.is_active:
                    print "tu usuario esta activo . . ."
                    #logout(request)
                    login(request,user)
                    #login(
                    print "You provided a correct username and password!"
                    return HttpResponseRedirect('/')
                    #nombres = user.first_name +" "+ user.last_name   
                    #return render_to_response("pagina.html",{'user':nombres})
                else:
                    print "Your account has been disabled!"
            else:
                print "Your username and password were incorrect."            
        else:
            form = LoginForm()
            print "error"
    else:
        form = LoginForm()
        
    return HttpResponseRedirect('/')
    

def getCiudad(latitud, longitud):
	v_r=1000
	v_rad = 1000
	v_ciudad = 'No ubicable'
	for ciudad in Ciudad.objects.order_by('-latitudCiudad', '-longitudCiudad'):
		v_latitud = abs(abs(ciudad.latitudCiudad) - abs(longitud))
		v_longitud = abs(abs(ciudad.longitudCiudad) - abs(latitud))
		v_distancia = v_latitud + v_longitud
		if v_r > v_distancia:
			v_r = v_distancia
			v_ciudad = ciudad.nombreCiudad
	return v_ciudad	    
