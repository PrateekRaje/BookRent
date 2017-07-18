from django.conf.urls import url

from home import views

urlpatterns = [
    url(r'^profile/$', views.profile, name='index'),
    url(r'^$', views.index, name='home'),
]
