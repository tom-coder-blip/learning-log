from django.urls import path, include
from . import views


app_name = 'accounts'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),  # Default auth URLs (login, logout)
     # Registration page.
    path('register/', views.register, name='register'),
]