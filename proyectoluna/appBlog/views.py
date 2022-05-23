from django.shortcuts import render
from appBlog.models import Post
from django.views.generic import ListView #Clases basadas en vistas CRUD
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

# Create your views here.
def Blog(request):
    posts=Post.objects.all()
    return render(request, "blog/blog.html", {"posts": posts})

class blogList(ListView):
    model: Post
    template_name = "blog/blog_list.html"

class blogDetalle(DetailView):
    model: Post
    template_name = "appBlog/blog_detalle.html"

class blogCreacion(CreateView):
    model: Post
    success_url = "/appBlog/blog/list"
    fields = ['titulo','subtitulo']

class blogUpdate(UpdateView):
    model: Post
    success_url = "/appBlog/blog/list"
    fields = ['titulo','subtitulo']

class blogDelete(DeleteView):
    model = Post
    success_url = "/appBlog/blog/list"

