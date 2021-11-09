from django.urls import path
from . import views # Import function from views.py of current folder
from .views import PostListView, PostDetailView


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('blog/', PostListView.as_view(), name='blog-blog'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), #post/primary-key id for the blog post
    path('about/', views.about, name='blog-about'), # since this is nested within 'blog', the full path to this page will be /blog/about
]
