from django.shortcuts import render, redirect,get_object_or_404
from .models import Blog
import datetime
# Create your views here.
def index(request):
    blog = Blog.objects
    return render(request, 'index.html',{'blog':blog})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.category = request.GET['category']
    blog.save()
    return redirect('/')

def update(request, id):
    blog = get_object_or_404(Blog, pk=id)
    return render(request, 'update.html',{'blog':blog})

def renew(request, id):
    blog = get_object_or_404(Blog, pk=id)
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.category = request.GET['category']
    blog.date = datetime.datetime.now()
    blog.save()
    return redirect('/detail/'+str(id))

def detail(request, id):
    blog = get_object_or_404(Blog, pk=id)
    return render(request, 'detail.html', {'blog':blog})

def delete(request, id):
    blog = get_object_or_404(Blog, pk=id)
    blog.delete()
    return redirect('/')