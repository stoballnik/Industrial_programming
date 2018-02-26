from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('', views.complete, name='complete'),
    path('deletecomplete', views.deleteComplete, name='deleteComplete'),
    path('deleteall', views.deleteAll, name='deleteAll')
]
