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
	url(r'^$', 'robame.views-cristhian.index'),
	url(r'^login/$', 'robame.views-ray.loginView'),
	url(r'^faq/', 'robame.views-cristhian.faq'),
	url(r'^mas/', 'robame.views-cristhian.mas'),
	url(r'^inscripcion/', 'robame.views-ray.registroUser'),
    url(r'^admin/', include(admin.site.urls)),
)
