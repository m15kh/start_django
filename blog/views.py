from django.shortcuts import render, get_object_or_404
# Create your views here.
from blog.models import Post
def blog_view(request):
    posts  = Post.objects.filter(status=1)
    context = {'posts':posts}
    return render(request, "blog/blog-home.html", context)

def blog_single(request, pid):
    post = get_object_or_404(Post, id=pid, status = 1)
    context = {'post':post}
    return render(request, "blog/blog-single.html", context)

def test(request,pid):
    
    # post = Post.objects.get(id=pid)
    post = get_object_or_404(Post, id=pid)
    context = {'post':post}
    return render(request, "test.html", context )  