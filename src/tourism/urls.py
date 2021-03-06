"""tourism URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.views.decorators.cache import cache_page
from apps.sitemaps import SITEMAPS
from django.shortcuts import render


FIVE_DAYS = 5 * 24 * 60 * 60

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^contact/', include('apps.contact.urls')),
    url(r'^', include('apps.posts.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += [
    url(r'^sitemap\.xml$', cache_page(FIVE_DAYS)(sitemap),
        {'sitemaps': SITEMAPS}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^robots\.txt$', lambda request: render(request, 'robots.txt'),
        name="home"),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns + static(settings.MEDIA_URL,
                             document_root=settings.MEDIA_ROOT)
