#-*- coding:UTF-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from robame.models import Asalto, Tag, Ciudad
from robame.forms import AsaltoForm
from django.template import RequestContext

def faq(request):
	return render_to_response('faq.html',{})

def mas(request):
	return render_to_response('mas.html',{})

def index_(request, id):
	return HttpResponseRedirect('/')
	
def index(request):
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
			context = {'asaltoForm': asaltoForm, 'envioValido': False}
			return render_to_response('index.html',context)
	else:
		comentarios = getComentarios()
		if comentarios.count >= 3:
			comentarios = comentarios[:3]
		context = {'asaltoForm': form, 'envioValido': True, 'comentarios': comentarios}
		return render_to_response('index.html',context)

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
		
def saveTags(descripcion, id_):
	array = descripcion.split(" ")
	for item in array:
		if item.startswith("#"):
			tag = Tag(descripcion = item, asalto_id = id_)
			tag.save()

def getComentarios():
	comentarios = []
	for asalto in Asalto.objects.order_by('-fecha', '-hora'):		
		comentarios.append({'fecha':asalto.fecha, 'hora':asalto.hora, 'descripcion': asalto.descripcion, 'ciudad': getCiudad(asalto.latitud, asalto.longitud)})
	return comentarios
	
def inscripcion(request):
	return render_to_response('inscripcion.html',{})
