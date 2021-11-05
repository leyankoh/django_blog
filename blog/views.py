from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# For now create a list of dictionaries which will contain the content of blog posts
posts = [

    {
        'author': 'Kylie',
        'title': 'Post 1',
        'content': 'Yep content',
        'date_posted': '5 November, 2021' # Pass a String for now
    }, 
    {
        'author': 'Not Kylie',
        'title': 'Post 2',
        'content': 'Mudkips are cute',
        'date_posted': '5 November, 2021' # Pass a String for now
    }, 

]

#make a home page
def home(request):
    context = {
        'posts': posts
    }

    # Passing the context will allow us to use those values within the template.
    return render(request, 'blog/home.html', context) # render the html page in templates/blog/home.html

# make an about page
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})