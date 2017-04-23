from django.conf.urls import url
from apps.posts import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/$', views.search, name='search'),
    url(r'^(?P<category_slug>[\-\w]+)/$', views.show_cat, name='category'),
    url(r'^(?P<category_slug>[\-\w]+)/(?P<article_slug>[\-\w]+)\.html$',
        views.show_article, name='article'),
]
