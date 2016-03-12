from django.conf.urls import patterns, url
from explorer import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^index/(?P<sidebar>[a-z]{4})',views.index,  name='arg_index'),
        url(r'^sidebar/favourites',views.favourites_sidebar,  name='favourites_sidebar'),
        url(r'^sidebar/search',views.search_sidebar,  name='search_sidebar'),
        url(r'^results/$', views.results, name='results'),
        )