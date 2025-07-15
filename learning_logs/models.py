from django.db import models
from django.contrib.auth.models import User

#The models.py defines the database structure for your Django application. It contains the Topic and Entry classes, which represent the main data your application works with.
#It hold all the data for Topic and Entry

# Create your models here.
class Topic(models.Model):   #Topic Class: Represents a topic that the user is learning about.

    """A topic the user is learning about."""
    text = models.CharField(max_length=200)  # Stores the topic name, Short text field (max 200 chars) 
    date_added = models.DateTimeField(auto_now_add=True)  # Stores the date & time when the topic was created.
    owner = models.ForeignKey(User, on_delete=models.CASCADE) #This links each topic to the user who created it

    def __str__(self):
        """Return a string representation of the model."""
        return self.text   #Returns the topic name (text) when the model instance is printed or displayed.
    

class Entry(models.Model):
    """Something specific learned about a topic."""
    
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)  # Links each entry to a topic
    text = models.TextField()  # Stores user input (no length limit)
    date_added = models.DateTimeField(auto_now_add=True)  # Stores timestamp when entry is created 

    class Meta:
        verbose_name_plural = 'entries'  # Ensures "Entries" is used instead of "Entrys"   

    def __str__(self):
        """Return a short preview of the entry."""
        if len(self.text) > 50: #Activity 1
            return f"{self.text[:50]}..."  # Displays the first 50 characters with an ellipsis
        return self.text #shows the full text if its 50 characters or less