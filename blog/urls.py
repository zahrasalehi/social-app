from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^create-posts/', views.create_posts, name='create_post'),
    url(r'^posts/', views.posts, name='posts')
]
