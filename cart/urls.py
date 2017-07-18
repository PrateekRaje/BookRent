from django.conf.urls import url

from cart import views


urlpatterns = [
    url(r'^rent/(?P<book_id>\d+)', views.add_to_cart, name='added-to-cart'),
    url(r'^cartview/', views.view_cart, name='cart-view'),
    url(r'^deletecart/(?P<items_id>\d+)',views.delete_from_cart, name='delete-cart')
]