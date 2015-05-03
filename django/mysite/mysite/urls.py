from django.conf.urls import patterns, include, url
from django.contrib import admin
import views
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.control, name='index'),
    url(r'^login$', views.login_page, name='login'),
    url(r'^logout$', views.logout_page, name='logout'),
    )
