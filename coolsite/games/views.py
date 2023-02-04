from django.http import HttpResponse, HttpResponseNotFound, Http404,HttpResponseForbidden,HttpResponseBadRequest,HttpResponseServerError
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse("Games")

def categories(request,carid):
    if(request.GET):
        print(request.GET)
    return HttpResponse(f"<h1>Cars</h1><p> {carid}</p>")

def archive(request,year):
    if int(year)>2023:
        return redirect('home', permanent=False)

    return HttpResponse(f"<h1>Архив по годам </h1><p>{year}</p>")

def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def Forbidden(request,exception):
    return HttpResponseForbidden('<h1>Доступ запрещен </h1>')

def BadRequest(request,exception):
    return HttpResponseBadRequest('<h1>Не правильный запрос </h1>')

def ServerError(request):
    return HttpResponseServerError('<h1>Ошибка сервера </h1>')


