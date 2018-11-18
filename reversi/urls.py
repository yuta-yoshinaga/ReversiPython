from django.conf.urls import url
from . import views
 
urlpatterns = [
#    url(r'^template/', views.index_template, name='index_template'),
    url('', views.index_template, name='index_template'),
]