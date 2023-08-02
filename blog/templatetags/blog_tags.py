from django import template
from blog.models import Post, Category

register = template.Library()

@register.simple_tag(name="posts")
def function():
    posts = Post.objects.filter(status=1)
    return posts

@register.inclusion_tag("blog/latest_posts.html")
def latest_posts():
    posts = Post.objects.filter(status=1).order_by("-published_date")[:3]
    return {'posts': posts}

@register.inclusion_tag("blog/category_wedget.html")
def wedget_category():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dic = {}
    for name in categories:
        cat_dic[name] = posts.filter(category=name).count()

    return {'categories': cat_dic}




