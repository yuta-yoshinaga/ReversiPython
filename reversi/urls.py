from django.conf.urls import url
from . import views
 
urlpatterns = [
    url(r'^FrontController', views.frontController, name='frontController'),
    url('', views.index_template, name='index_template'),
]