from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.



class Post(models.Model):
    # Create a model to contain our blog post data
    # Remember that a user can have multiple posts but a post can only have one author
    # If we enter python manage.py sqlmigrate blog 0001 (i.e. referring to the 0001_initial.py file) then the 
    # system will write the SQL that will make a table to contain our data
    
    # Functions to know
    # Grab a username User.objects.filter(username='___').first() will return <User: ___ >
    # This variable will also contain the ID of said user (user.id) (Assuming user is the variable you store the author's user in)
    # So you can create a post specifying Post (title = " ", content = " ", author = user.id)
    # ModelName.save() then saves all the content to that model

    # Django also allows you to modify contents of your model with .modelname_set function
    # In this instance, we can access the model using <user>.post_set to create an object tied to that user.

    # user.post_set.all(): Lists all posts under the user
    # user.post_set.create(...): Creates a post under the "user" that you stored.

    title = models.CharField(max_length=100) # Create a title field for the blog post
    content = models.TextField()
    
    # auto_now updates the date of the post to the exact time it was modified
    date_posted = models.DateTimeField(default=timezone.now) 
    
    # Make the author a foreign key
    # If the user is delete then delete the post as well, but not the other way around
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title