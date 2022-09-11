from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def render_post(request):
    posts = Post.objects.all()
    return render(request, 'post.html', {'posts': posts})

def render_post_detail(request, post_id):
    post_detail=get_object_or_404(Post, pk=post_id)
    return render(request, 'post_detail.html', {'post': post_detail})