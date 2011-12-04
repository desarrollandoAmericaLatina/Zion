#-*- coding:utf-8 -*-
#-*- coding:UTF-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from robame.forms import AsaltoForm
from django.template import RequestContext


def faq(request):
	return render_to_response('faq.html',{})

def mas(request):
	return render_to_response('mas.html',{})

def index(request):
		form = AsaltoForm()
		if request.method == 'POST':
			asaltoForm = AsaltoForm(request.POST)
			if asaltoForm.is_valid():
				asaltoForm.save()
				return HttpResponseRedirect('/')
			else:
				context = {'asaltoForm': asaltoForm, 'envioValido': False}
				return render_to_response('index.html',context)
		else:
			context = {'asaltoForm': form, 'envioValido': True}
			return render_to_response('index.html',context)

def inscripcion(request):
	return render_to_response('inscripcion.html',{})
