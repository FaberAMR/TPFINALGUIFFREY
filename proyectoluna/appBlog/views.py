from django.shortcuts import render
from appBlog.models import Post

# Create your views here.
def Blog(request):
    posts=Post.objects.all()
    return render(request, "blog/blog.html", {"posts": posts})

