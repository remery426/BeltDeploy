from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', (views.index)),
    url(r'logout$', views.logout),
    url(r'createapt$',views.createapt),
    url(r'delete/(?P<id>\d*)$', views.delete),
    url(r'editpage/(?P<id>\d*)$', views.editpage),
    url(r'edit/(?P<id>\d*)$', views.edit)
    ]
