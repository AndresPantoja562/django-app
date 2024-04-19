from django.urls import path

from . import views

urlpatterns = {
    path ("1", views.index, name='index'),
    path ("list", views.list_persons, name='list'),


}