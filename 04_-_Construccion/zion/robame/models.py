#-*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User, UserManager
import datetime

class Usuario(User):
	objects = UserManager()
	def __unicode__(self):
		return '%s' % (self.username)

class Ciudad(models.Model):
	codigoCiudad = models.CharField(max_length=6, verbose_name="Centro poblado", help_text="Indique el código del centro poblado", null=False, blank=False, primary_key=True)
	latitudCiudad = models.DecimalField(max_digits=17, decimal_places=15, verbose_name="Latitud", help_text="Indique la latitud")
	longitudCiudad = models.DecimalField(max_digits=17, decimal_places=15, verbose_name="Longitud", help_text="Indique la longitud")
	nombreCiudad = models.CharField(max_length=80, verbose_name="Ciudad", help_text="Indique el nombre de la ciudad")
	departamento = models.CharField(max_length=80, verbose_name="Departamento", help_text="Indique el nombre del departamento")
	provincia = models.CharField(max_length=80, verbose_name="Provincia", help_text="Indique el nombre de la provincia")
	distrito = models.CharField(max_length=80, verbose_name="Distrito", help_text="Indique el nombre del distrito")
	def __unicode__(self):
		return '%s' % (self.codigoCiudad)

class Asalto(models.Model):
	latitud = models.DecimalField(max_digits=17, decimal_places=15, verbose_name="Latitud", help_text="Indique la latitud")
	longitud = models.DecimalField(max_digits=17, decimal_places=15, verbose_name="Longitud", help_text="Indique la longitud")
	fecha = models.DateField(default=datetime.date.today(), verbose_name="Fecha", help_text="Indique la fecha")
	hora = models.TimeField(default=datetime.datetime.today().time(), max_length=12, verbose_name="Hora", help_text="Indique la hora")
	descripcion = models.TextField(max_length=160, blank=False)
	def __unicode__(self):
		return '%s' % (self.descripcion)

class Punto(models.Model):
	latitudCiudad = models.DecimalField(max_digits=13, decimal_places=11, unique=True, blank=False)
	longitudCiudad = models.DecimalField(max_digits=13, decimal_places=11, unique=True, blank=False)
	descripcion = models.TextField(blank=False)
	usuario = models.ForeignKey(User)
	ciudad = models.ForeignKey(Ciudad)
	def __unicode__(self):
		return '%s' % (self.descripcion)
	
class Tag(models.Model):
	descripcion = models.CharField(max_length=160, verbose_name="Tag", help_text="Indique el tag", null=False, blank=False)
	asalto = models.ForeignKey(Asalto)
	def __unicode__(self):
		return '%s' % (self.descripcion)
