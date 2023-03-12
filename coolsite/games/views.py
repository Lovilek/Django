from django.http import HttpResponse, HttpResponseNotFound, Http404,HttpResponseForbidden,HttpResponseBadRequest,HttpResponseServerError
from django.shortcuts import render, redirect, get_object_or_404

from .form import *
from .models import *

menu=[
    {'title':"О сайте",'url_name':'about'},
    {'title':"Добавить статью",'url_name':'add_page'},
    {'title':"Обратная связь",'url_name':'contact'},
    {'title':"Войти",'url_name':'login'}

]

def index(request):
    posts=Games.objects.all()

    context={
        'posts':posts,
        'menu':menu,
        'title': 'Главная страница',
        'cat_selected':0,
    }
    return render(request, 'games/index.html',context=context)

def about(request):
    return render(request, 'games/about.html',{'title': 'About','menu':menu})

def addpage(request):
    if request.method=='POST':
        form=AddPostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return  redirect('home')

    else:
        form=AddPostForm()
    return render(request,'games/addpage.html',{'form':form,'menu':menu,'title':'Добавление статьи'})

def contact(request):
    return HttpResponse("Обратная связь")

def show_post(request,post_slug):
    post=get_object_or_404(Games,slug=post_slug)
    context={
        'post':post,
        'menu':menu,
        'title':post.title,
        'cat_selected':post.cat_id,
    }

    return render(request,'games/post.html',context=context)
def show_category(request,cat_id):
    posts = Games.objects.filter(cat_id=cat_id)

    if len(posts)==0:
        raise Http404()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': cat_id,
    }
    return render(request, 'games/index.html', context=context)
def login(request):
    return HttpResponse("Авторизация")

def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def Forbidden(request,exception):
    return HttpResponseForbidden('<h1>Доступ запрещен </h1>')

def BadRequest(request,exception):
    return HttpResponseBadRequest('<h1>Не правильный запрос </h1>')

def ServerError(request):
    return HttpResponseServerError('<h1>Ошибка сервера </h1>')


