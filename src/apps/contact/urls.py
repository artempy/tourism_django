from django.conf.urls import url
from apps.contact import views


urlpatterns = [
    url(r'^$', views.contact_form, name='contact'),
]
