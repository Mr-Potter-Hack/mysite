from django.shortcuts import render
from datetime import datetime
from .models import Contact, Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .forms import PostForm, EditForm
from django.urls import reverse_lazy


def index(request):
    return render(request, "index.html")
    #return HttpResponse("Hello, world.")

def websites(request):
    return render(request, "websites.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        description = request.POST.get('description')
        contact = Contact(name=name, email=email, phone=phone, 
        description=description, date=datetime.today())
        contact.save()
    return render(request, "contact.html")

def clock(request):
    return render(request, "clock.html")

def todo(request):
    return render(request, "todo.html")

#def blog(request):
#    return render(request, "blog.html")

class BlogView(ListView):
    model = Post
    template_name = 'blog.html'

class postdetailview(DetailView):
    model = Post
    template_name = 'post_1_detailed.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    #fields = ['title', 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('blog')
