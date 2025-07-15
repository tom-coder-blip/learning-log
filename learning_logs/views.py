#This view handles the request for the home page. It renders the index.html template.
#Fetches data from models.py and sends it to HTML templates

from django.shortcuts import render, redirect # Import the render function to render HTML templates
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.

def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html') # Render the 'index.html' template from the 'learning_logs' app 

@login_required
def topics(request):
    """Show all topics for the logged_in user."""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added') #ensures that users see only their own topics
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    # Make sure the topic belongs to the current user.
    
    if topic.owner != request.user:
        raise Http404 #Prevents unauthorized access/ user can't view a topic that is not assigned to them
    
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries} 
    return render(request, 'learning_logs/topic.html', context) 

#for the form to add a new topic
@login_required
def new_topic(request):
    """Add a new topic associated with the logged-in user."""
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)  # Don't save to DB yet
            new_topic.owner = request.user  # Assign logged-in user
            new_topic.save()  # Save to DB
            return redirect('learning_logs:topics')  # Redirect to topics page
    else:
        form = TopicForm() 

    # Render the form  
    return render(request, 'learning_logs/new_topic.html', {'form': form}) 

#for the form to add a new entry
@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # Display a blank form
        form = EntryForm()
    else:
        # Process submitted form data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)  # Create object without saving
            new_entry.topic = topic  # Assign topic to the entry
            new_entry.save()  # Now save to database
            return redirect('learning_logs:topic', topic_id=topic_id)  # Redirect to topic page

    # Show the form (blank or invalid)
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Display the form with the current entry pre-filled
        form = EntryForm(instance=entry)
    else:
        # Process the submitted form
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context) 

@login_required
def delete_entry(request, entry_id):
    """Delete an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method == 'POST':
        entry.delete()
        return redirect('learning_logs:topic', topic_id=topic.id)
    else:
        # Show confirmation page
        context = {'entry': entry, 'topic': topic}
        return render(request, 'learning_logs/delete_entry.html', context)

@login_required   
def delete_topic(request, topic_id):
    """Delete a topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404

    if request.method == 'POST':
        topic.delete()
        return redirect('learning_logs:topics')
    else:
        # Show confirmation page
        context = {'topic': topic}
        return render(request, 'learning_logs/delete_topic.html', context)

