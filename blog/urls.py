from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^create-posts/', views.create_posts, name='create_post'),
    url(r'^(?P<pk>[0-9]+)/$', views.post_detial, name='post_detail'),
    url(r'^posts/', views.posts, name='posts'),
    url(r'^category/', views.category_list, name='category_list'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category_detail, name='category_detail')

]
