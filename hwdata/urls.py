from django.conf.urls import url
from . import views

urlpatterns = [
    # /hwdata/
    url(r'^$', views.index, name='index'),
    # /hwdata/json/
    url(r'^json', views.json, name='json'),
]
