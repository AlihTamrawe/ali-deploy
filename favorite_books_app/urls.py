from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index),    
    path('<int:id>/',views.like),
    path('like/int:id>/',views.do_like)
]