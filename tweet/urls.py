from django.urls import path
from . import views

urlpatterns = [
    path("tweet/",views.index,name='index')
]
