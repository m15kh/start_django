from django.shortcuts import render, get_object_or_404
# Create your views here.
from blog.models import Post
def blog_view(request, cat_name = None, author_username = None):
    posts = Post.objects.filter(status=1) 
    if cat_name :
        posts = posts.filter(post_category__name=cat_name)
    if author_username :
        posts = posts.filter(author__username = author_username)
    context = {'posts':posts}
    return render(request, "blog/blog-home.html", context)

def blog_single(request, pid): 
    post = get_object_or_404(Post, id=pid, status = 1)
    context = {'post':post}
    return render(request, "blog/blog-single.html", context)

def test(request):
    # post = Post.objects.get(id=pid)
    return render(request, "test.html")   
 
def blog_category(request, cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(post_category__name=cat_name)
    context = {'posts': posts}
    return render(request, "blog/blog-home.html", context) 

def blog_search(request):
    print("hello world")
    print(request)
    print("goof bye")
    posts = Post.objects.filter(status=1) 
    context = {'posts':posts}
    return render(request, "blog/blog-home.html", context)

