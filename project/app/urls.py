from django.urls import path
from app import views

urlpatterns = [
    path('home/',views.home ,name="home"),
    path('collection/',views.collection,name="collection"),
    path('myfilter/' ,views.myfilter,name="myfilter")
]
