from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'dontbeadick.views.index', name='index'),
    url(r'^(?P<drawing_id>\d+)/$', 'dontbeadick.views.show_drawing', name='show_drawing'),
    url(r'^about/$', 'dontbeadick.views.about', name='about'),
    # url(r'^dontbeadick/', include('dontbeadick.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
