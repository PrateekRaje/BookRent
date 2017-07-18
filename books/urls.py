from django.conf.urls import url

from books import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^books/$', views.book_list, name='books'),
    url(r'^book/(?P<pk>\d+)$', views.book_detail, name='book-detail'),
    url(r'^authors/$', views.author_list, name='authors'),
    url(r'^author/(?P<pk>\d+)$', views.author_detail, name='author-detail'),
    url(r'^check/(?P<book_id>\d+)', views.checkAvailability, name='check-availability'),
]    