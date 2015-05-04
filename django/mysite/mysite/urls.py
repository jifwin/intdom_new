from django.conf.urls import patterns, include, url
from django.contrib import admin
import views
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login_page, name='login'),
    url(r'^logout$', views.logout_page, name='logout'),
    url(r'^control/(?P<device>\d{2})/(?P<action>[a-z]+)/$', views.control, name='control'),
    url(r'^light_sensor',views.send_light,name='light_sensor')
    )
