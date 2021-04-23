from django.shortcuts import render
from datetime import datetime
from .models import Contact, Post
from django.views.generic import ListView, DetailView
# Create your views here.
from django.http import HttpResponse


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

#def blog(request):
#    return render(request, "blog.html")

class BlogView(ListView):
    model = Post
    template_name = 'blog.html'

class postdetailview(DetailView):
    model = Post
    template_name = 'post_1_detailed.html'