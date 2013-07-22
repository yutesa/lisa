from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lisa.views.home', name='home'),
    # url(r'^lisa/', include('lisa.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'yutesapp.views.inicio'),
    url(r'^Products/', 'yutesapp.views.Productos'),
    url(r'^Products/AddLike$', 'yutesapp.views.DarLike', name='DarLike'),
)