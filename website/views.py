from django.shortcuts import render
# Create your views here.

def index_view(request):
    return render(request, "website/index.html")

def contact_view(request):
    return render(request, "website/contact.html")

def about_view(request):
    return render(request, "website/about.html")

def test_view(request):
    context= {'name': 'mohammad', 'last':'khalili'}
    return render(request, "website/test.html", context)


