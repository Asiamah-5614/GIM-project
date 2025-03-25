from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404


# Create your views here.

def home(request):
    post_blog = Post.objects.order_by('-created_at')[:3]  # Get the latest 3 posts
    return render(request, 'index.html', {'post_blog': post_blog})

def about(request):
    return render(request, 'about_page.html', {})

def contact(request):
    return render(request, 'contacts.html', {})

def service(request):
    return render(request, 'our_service.html', {})

def post(request):
    post_ = Post.objects.order_by('-created_at')
    return render(request, 'blog.html', {'posts': post_})

def post_detail(request, slug):
    post_detail = get_object_or_404(Post, slug=slug)
    return render(request, 'blog_detail.html', {'blog': post_detail})

