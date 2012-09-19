from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'itdocs.views.home', name='home'),
    # url(r'^itdocs/', include('itdocs.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', 'finances.views.index'),
    url(r'^payments/$', 'finances.views.payments'),
    url(r'^payments/(?P<payment_id>\d+)/print/$', 'finances.views.payments_print'),
    url(r'^payments/(?P<payment_id>\d+)/edit/$', 'finances.views.payments_edit'),
    url(r'^admin/', include(admin.site.urls)),
)
