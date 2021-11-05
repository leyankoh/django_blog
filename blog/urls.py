from django.urls import path
from . import views # Import function from views.py of current folder


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'), # since this is nested within 'blog', the full path to this page will be /blog/about
]
