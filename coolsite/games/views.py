from django.http import HttpResponse, HttpResponseNotFound, Http404,HttpResponseForbidden,HttpResponseBadRequest,HttpResponseServerError
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView

from .form import *
from .models import *




menu=[
    {'title':"О сайте",'url_name':'about'},
    {'title':"Добавить статью",'url_name':'add_page'},
    {'title':"Обратная связь",'url_name':'contact'},
    {'title':"Войти",'url_name':'login'}

]

class GamesHome(ListView):
    model=Games
    template_name = 'games/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        context['menu']=menu
        context['title']='Главная страница'
        context['cat_selected']=0
        return context

    def get_queryset(self):
        return Games.objects.filter(is_published=True)

# def index(request):
#     posts=Games.objects.all()
#
#     context={
#         'posts':posts,
#         'menu':menu,
#         'title': 'Главная страница',
#         'cat_selected':0,
#     }
#     return render(request, 'games/index.html',context=context)

def about(request):
    return render(request, 'games/about.html',{'title': 'About','menu':menu})

# def addpage(request):
#     if request.method=='POST':
#         form=AddPostForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return  redirect('home')
#
#     else:
#         form=AddPostForm()
#     return render(request,'games/addpage.html',{'form':form,'menu':menu,'title':'Добавление статьи'})

class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'games/addpage.html'
    success_url = reverse_lazy('home')

    def get_context_data(self,*,object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='Добавление статьи'
        context['menu']=menu
        return context


def contact(request):
    return HttpResponse("Обратная связь")

class ShowPost(DetailView):
    model = Games
    template_name = 'games/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self,*,object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title']=context['post']
        context['menu']=menu
        return context

# def show_post(request,post_slug):
#     post=get_object_or_404(Games,slug=post_slug)
#     context={
#         'post':post,
#         'menu':menu,
#         'title':post.title,
#         'cat_selected':post.cat_id,
#     }
#
#     return render(request,'games/post.html',context=context)

class GamesCategory(ListView):
    model = Games
    template_name = 'games/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Games.objects.filter(cat__slug=self.kwargs['cat_slug'],is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='Категория - '+str(context['posts'][0].cat)
        context['menu']=menu
        context['cat_selected']=context['posts'][0].cat_id
        return context
# def show_category(request,cat_id):
#     posts = Games.objects.filter(cat_id=cat_id)
#
#     if len(posts)==0:
#         raise Http404()
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Главная страница',
#         'cat_selected': cat_id,
#     }
#     return render(request, 'games/index.html', context=context)
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


