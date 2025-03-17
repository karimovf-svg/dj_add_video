from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404, redirect
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .forms import UserLoginForm, NewsForm
from django.contrib import messages
from .models import *
import threading

def index(request):
    news = News.objects.all()
    category = Categories.objects.all()

    context ={
        "category": category,
        "news": news,
        "title":"News",
    }
    return render(request,'index.html', context=context)

def category_new(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Categories.objects.all()
    context = {
        "category": category,
        "news": news,
        "title": "News",
    }
    return render(request, 'cat_new.html', context=context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, files=request.FILES)
        if form.is_valid():
            file = request.FILES["video"]
            thread = threading.Thread(target=set_up_cloud, args=(file, form))
            thread.start()
            messages.success(request, "Created News")
            return redirect('home')
        else:
            messages.success(request, form.errors)
    else:
        form = NewsForm()
    return render(request, 'add_news.html', {'form': form})

def delete_news(request, news_id):
    news = get_object_or_404(News, id=news_id)
    news.delete()
    messages.success(request, "Deleted News")
    return redirect('home')

def set_up_cloud(file, instance):
    file_path = default_storage.save(file.name, ContentFile(file.read()))
    instance.video = file_path
    instance.save()
