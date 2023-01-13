from django.urls import path
from . import views

urlpatterns = [
    path('scrape/<str:url>/', views.scrape, name='scrape'),


