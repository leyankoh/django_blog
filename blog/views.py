from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponse
from .models import Post
# Create your views here.


#make a home page
def home(request):
    return render(request, 'blog/home.html')

# make an about page
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

class PostListView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    # have our template loop over "posts" instead of "object_list" (as specified in the home views above)
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3

class PostDetailView(DetailView):
    # Introduce a view for detailed posts
    # <app>/<model>_<viewtype>.html
    # Generic class-based views will look for a template named like the above
    # hence it will look for blog/post_detail.html by default
    model = Post


##### Unused Modules - left in for tutorial purposes ######
# Not required anymore - we're using postlistview and postdetailview
def blog(request):
    context = {
        'posts': Post.objects.all() # We can access all posts created under the Post model with this
    }

    # Passing the context will allow us to use those values within the template.
    return render(request, 'blog/blog.html', context) # render the html page in templates/blog/home.html
