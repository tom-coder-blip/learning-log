"""
URL configuration for ll_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# This file defines the main URL configurations for the project. It includes admin URLs and routes all other requests to the learning_logs app.

from django.contrib import admin  # Import Django's built-in admin module
from django.urls import path, include  # Import path for URL routing and include for including other URL configurations

urlpatterns = [
    path('admin/', admin.site.urls),  # Route for the Django admin panel (e.g., http://127.0.0.1:8000/admin/)
    path('accounts/', include('accounts.urls')), #Includes all authentication URLs
    path('', include('learning_logs.urls')),  # Include URL patterns from the 'learning_logs' app (handles user-defined routes)
]
