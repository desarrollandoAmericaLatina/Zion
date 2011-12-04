from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lemon.views.home', name='home'),
    # url(r'^lemon/', include('lemon.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	url(r'^$', 'robame.views.index'),
	url(r'^login/$', 'robame.views.loginView'),
	url(r'^faq/', 'robame.views.faq'),
	url(r'^mas/', 'robame.views.mas'),
	url(r'^inscripcion/', 'robame.views.registroUser'),
	url(r'^mapa/([^/]+)/([^/]+)/$', 'robame.views.coordenada'),
    url(r'^admin/', include(admin.site.urls)),
)
