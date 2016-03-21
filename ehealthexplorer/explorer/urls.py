from django.conf.urls import patterns, url
from explorer import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^sidebar/favourites',views.favourites_sidebar,  name='favourites_sidebar'),
        url(r'^sidebar/search/$',views.search_sidebar,  name='search_sidebar'),
        url(r'^results/$', views.results, name='results'),
        url(r'^sidebar/results/$', views.results_sidebar, name='results_sidebar'),
        url(r'^sidebar/profile', views.profile_sidebar, name='profile_sidebar'),
        url(r'^sidebar/shared/$', views.search_categories, name='search_categories'),
        url(r'^sidebar/login/$', views.user_login,name='login'),
)
