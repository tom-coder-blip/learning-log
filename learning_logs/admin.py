from django.contrib import admin

# Register your models here.
from .models import Topic, Entry

admin.site.register(Topic)
admin.site.register(Entry)

# This code first imports the model we want to register, Topic and Entry. The dot 
# in front of models tells Django to look for models.py in the same directory as 
# admin.py. The code admin.site.register() tells Django to manage our model 
# through the admin site.   

