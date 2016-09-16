from django.conf.urls import url
from . import views


app_name = 'dreamnight'
urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
]
