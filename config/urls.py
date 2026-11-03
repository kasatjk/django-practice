from django.urls import path
from .views import page1, page2, page3

urlpatterns = [
    path('1', page1, name="page1"),
    path('2', page2, name="page2"),
    path('3', page3, name="page3")
]
