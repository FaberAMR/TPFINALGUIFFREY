from django.urls import path
from . import views

urlpatterns = [
    path('blog/list', views.blogList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.blogDetalle.as_view(), name='Detail'),
    path(r'^nuevo', views.blogCreacion.as_view(), name='New'),
    path(r'editar/(?P<pk>\d+)$', views.blogUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.blogDelete.as_view(), name='Delete'),
    path('', views.Blog, name="Blog"), 
       
    ]
