# Create your views here.
from django.shortcuts import render_to_response

def faq(request):
	return render_to_response('faq.html',{})

def mas(request):
	return render_to_response('mas.html',{})

def index(request):
	return render_to_response('index.html',{})
