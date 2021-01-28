from django.urls import path
from . import views



urlpatterns = [
    path('', views.home,name='site-index'),
    path('/about', views.about,name='site-about'),
    path('/AISEC', views.about,name='site-AISEC'),
    path('/cit', views.about,name='site-cit'),
    path('/contact', views.about,name='site-contact'),
    path('/gallery', views.about,name='site-gallery'),
    path('/indtrip', views.about,name='site-indtrip'),
    path('/ITM', views.about,name='site-ITM'),
    path('/registration', views.about,name='site-registration'),
    path('/sponsors', views.about,name='site-sponsors'),
    path('/teachers', views.about,name='site-teachers'),
    path('/ITM', views.about,name='site-ITM'),


   
]