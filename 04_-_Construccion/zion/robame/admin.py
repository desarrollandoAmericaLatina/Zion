from django.contrib import admin
from robame.models import Usuario
from robame.models import Ciudad
from robame.models import Asalto
from robame.models import Punto
from robame.models import Tag

admin.site.register(Usuario)
admin.site.register(Ciudad)
admin.site.register(Asalto)
admin.site.register(Punto)
admin.site.register(Tag)
