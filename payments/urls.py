from django.conf.urls import url

from payments import views


urlpatterns = [
    url(r'^pay/(?P<price>\d+)$', views.pay, name='payment'),
]
    