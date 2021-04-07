from django.urls import path
from . import views



urlpatterns = [
    path('', views.home,name='site-index'),
    path('about/', views.about,name='site-about'),
    path('AISEC/', views.AISEC,name='site-AISEC'),
    path('cit/', views.cit,name='site-cit'),
    path('contact/', views.contact,name='site-contact'),
    path('gallery/', views.gallery,name='site-gallery'),
    path('indtrip/', views.indtrip,name='site-indtrip'),
    path('registration/', views.registration,name='site-registration'),
    path('sponsors/', views.sponsors,name='site-sponsors'),
    path('teachers/', views.teachers,name='site-teachers'),
    path('ITM/', views.ITM,name='site-ITM'),


   
]