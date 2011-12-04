# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from robame.models import Asalto, Tag, Ciudad
from robame.forms import AsaltoForm, LoginForm,formUser
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
			send_mail('Creación de cuenta - roba.me', mensaje, 'no-reply@robame.pe', [correo], fail_silently=False)
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
	form = AsaltoForm()
	if request.method == 'POST':
		asaltoForm = AsaltoForm(request.POST)
		if asaltoForm.is_valid():
			descripcion_ = asaltoForm.cleaned_data['descripcion']
			asaltoForm.save()
			asalto = Asalto.objects.order_by('-id')[:1]
			saveTags(descripcion_, asalto[0].id)
			return HttpResponseRedirect('/')
		else:
			context = {'asaltoForm': asaltoForm,'isLogin':isLogin,'loginForm':LoginForm(), 'envioValido': False}
			return render_to_response('index.html',context)
	else:
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

def faq(request):
	comentarios = getComentarios()
	if comentarios.count >= 3:
		comentarios = comentarios[:3]
	context = { 'comentarios': comentarios}
	return render_to_response('faq.html',context)

def mas(request):
	comentarios = getComentarios()
	if comentarios.count >= 10:
		comentarios = comentarios[:10]
	context = { 'comentarios': comentarios}
	return render_to_response('mas.html',context)

def index_(request, id):
	return HttpResponseRedirect('/')
	
def index(request):
	user = request.user
	if user is not None and user.is_active:
		isLogin = True
	else:
		isLogin = False
		
	form = AsaltoForm()
	if request.method == 'POST':
		asaltoForm = AsaltoForm(request.POST)
		if asaltoForm.is_valid():
			descripcion_ = asaltoForm.cleaned_data['descripcion']
			asaltoForm.save()
			asalto = Asalto.objects.order_by('-id')[:1]
			saveTags(descripcion_, asalto[0].id)
			return HttpResponseRedirect('/')
		else:
			context = {'asaltoForm': asaltoForm,'isLogin':isLogin,'loginForm':LoginForm(), 'envioValido': False}
			return render_to_response('index.html',context)
	else:
		comentarios = getComentarios()
		if comentarios.count >= 3:
			comentarios = comentarios[:3]
		context = {'asaltoForm': form, 'envioValido': True, 'isLogin':isLogin,'loginForm':LoginForm(),'comentarios': comentarios}
		return render_to_response('index.html',context)

def getCiudad(latitud, longitud):
	v_r=1000
	v_rad = 1000
	v_ciudad = 'No ubicable'
	_latitud = 0
	_longitud = 0
	for ciudad in Ciudad.objects.order_by('-latitudCiudad', '-longitudCiudad'):
		v_latitud = abs(abs(ciudad.latitudCiudad) - abs(longitud))
		v_longitud = abs(abs(ciudad.longitudCiudad) - abs(latitud))
		v_distancia = v_latitud + v_longitud
		if v_r > v_distancia:
			v_r = v_distancia
			v_ciudad = ciudad.nombreCiudad
			_latitud = ciudad.latitudCiudad
			_longitud = ciudad.longitudCiudad
	return [v_ciudad, _latitud, _longitud]
	
def saveTags(descripcion, id_):
	array = descripcion.split(" ")
	for item in array:
		if item.startswith("#"):
			tag = Tag(descripcion = item, asalto_id = id_)
			tag.save()

def getComentarios():
	comentarios = []
	for asalto in Asalto.objects.order_by('-fecha', '-hora'):
		[ciudad, latitud, longitud] = getCiudad(asalto.latitud, asalto.longitud)
		comentarios.append({'fecha': asalto.fecha, 'hora': asalto.hora, 'descripcion': asalto.descripcion, 'ciudad': ciudad, 'ciudad_latitud': latitud, 'ciudad_longitud': longitud})
	return comentarios
	
def inscripcion(request):
	comentarios = getComentarios()
	if comentarios.count >= 3:
		comentarios = comentarios[:3]
	context = { 'comentarios': comentarios}
	return render_to_response('inscripcion.html',context)

def coordenada(request, latitud, longitud):
	user = request.user
	if user is not None and user.is_active:
		isLogin = True
	else:
		isLogin = False
		
	form = AsaltoForm()
	if request.method == 'POST':
		asaltoForm = AsaltoForm(request.POST)
		if asaltoForm.is_valid():
			descripcion_ = asaltoForm.cleaned_data['descripcion']
			asaltoForm.save()
			asalto = Asalto.objects.order_by('-id')[:1]
			saveTags(descripcion_, asalto[0].id)
			return HttpResponseRedirect('/')
		else:
			context = {'asaltoForm': asaltoForm,'isLogin':isLogin,'loginForm':LoginForm(), 'envioValido': False}
			return render_to_response('index.html',context)
	else:
		comentarios = getComentarios()
		if comentarios.count >= 3:
			comentarios = comentarios[:3]
		context = {'asaltoForm': form, 'envioValido': True, 'isLogin':isLogin,'loginForm':LoginForm(),'comentarios': comentarios, 'coordenada': True, 'latitud': latitud, 'longitud': longitud}
		return render_to_response('index.html',context)
