#hold any catalog specific urls
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
]