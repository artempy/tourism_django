from django.conf.urls import url
from apps.posts import views
from django.views.decorators.cache import cache_page


FIVE_DAYS = 5 * 24 * 60 * 60

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/$', views.search, name='search'),
    url(r'^(?P<category_slug>[\-\w]+)(/page/(?P<page>[1-9][0-9]?))?/$',
        cache_page(FIVE_DAYS)(views.ShowCat.as_view(paginate_by=7)),
        name='category'),
    url(r'^(?P<category_slug>[\-\w]+)/(?P<article_slug>[\-\w]+)\.html(/comments/page/(?P<page>[1-9][0-9]?))?/?$',
        views.show_article, name='article'),
]
