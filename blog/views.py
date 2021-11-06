from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.


#make a home page
def home(request):
    context = {
        'posts': Post.objects.all() # We can access all posts created under the Post model with this
    }

    # Passing the context will allow us to use those values within the template.
    return render(request, 'blog/home.html', context) # render the html page in templates/blog/home.html

# make an about page
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})