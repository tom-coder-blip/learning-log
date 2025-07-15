#This file defines URL patterns for the learning_logs app. The app_name ensures URLs dont conflict with other apps
"""Defines URL patterns for learning_logs."""

from django.urls import path  # Import path function for defining URL patterns
from . import views  # Import views from the current app

app_name = 'learning_logs'  # Namespace for the app (useful for distinguishing URLs in templates)

urlpatterns = [
    # Home page
    path('', views.index, name='index'),  # URL pattern mapping to the home page, calls the 'index' view 
     # Page that shows all topics.
    path('topics/', views.topics, name='topics'), # List all topics
    # Detail page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),# View specific topic
    # Page for adding a new topic.
    path('new_topic/', views.new_topic, name='new_topic'), # Add a new topic 
    # Existing paths...
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page for editing an entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),

    path('delete_entry/<int:entry_id>/', views.delete_entry, name='delete_entry'),

    path('delete_topic/<int:topic_id>/', views.delete_topic, name='delete_topic')  # Delete a topic
] 