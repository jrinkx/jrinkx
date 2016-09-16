from django.conf.urls import url
from . import views


app_name = 'blog'

urlpatterns = [
    url(r'^blog/admin$', views.blog_admin, name='blog_admin'),
    url(r'^blog$', views.blog_posts, name='blog_posts'),
    url(r'^blog/new$', views.create_post, name='create_post'),
    url(r'^blog/edit/(?P<pk>\d+)$', views.update_post, name='update_post'),
    url(r'^blog/delete/(?P<pk>\d+)$', views.delete_post, name='delete_post'),
]
