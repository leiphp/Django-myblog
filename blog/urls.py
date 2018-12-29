from django.conf.urls import url
from . import views

app_name='blog'
urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^article/(?P<article_id>[0-9]+)$', views.article_page, name='article_page'),
]
