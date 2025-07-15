from django import forms  
from .models import Topic, Entry

class TopicForm(forms.ModelForm):  
    """Form for adding a new topic."""  
    class Meta:  
        model = Topic  # Use the Topic model  
        fields = ['text']  # Include only the 'text' field  
        labels = {'text': ''}  # Remove the default label  

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}  # Removes label
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}  # Increases text area size