from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render
from .models import *

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'},
]


def index(request):
    context = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': Women.objects.all(),
        'cats': Category.objects.all(),
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=context)


def about(request):
    context = {
        'title': 'О сайте',
        'menu': menu,
    }
    return render(request, 'women/about.html', context=context)


def addpage(request):
    return HttpResponse('Добавление статьи')


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def pageNotFound(request):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id = {post_id}')


def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)
    if len(posts) == 0:
        raise Http404()
    cats = Category.objects.all()
    context = {
        'title': 'Отоброжение по рубрикам',
        'menu': menu,
        'posts': posts,
        'cats': cats,
        'cat_selected': cat_id,
    }
    return render(request, 'women/index.html', context=context)
