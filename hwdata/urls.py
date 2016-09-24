from django.conf.urls import url
from . import views

app_name = 'hwdata'

urlpatterns = [
    # /hwdata/
    url(r'^$', views.index, name='index'),
    # /hwdata/json/
    url(r'^json', views.json, name='json'),
]
