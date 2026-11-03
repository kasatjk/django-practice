from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # Головні розділи
    path('about-city/', views.about_city, name='about-city'),
    path('about-city/city-facts/', views.city_facts, name='city-facts'),
    path('about-city/city-data/', views.city_data, name='city-data'),
    
    path('about-me/', views.about_me, name='about-me'),
    path('about-me/me-bio/', views.me_bio, name='me-bio'),
    path('about-me/me-facts/', views.me_facts, name='me-facts'),
]

