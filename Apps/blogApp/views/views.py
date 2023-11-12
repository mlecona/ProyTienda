""" Vistas de Pagina blogs """

from django.shortcuts import render
from Apps.blogApp.models import Post, Categoria


def blog(request):
    """ funcion de blog """
    mipost = Post.objects.all()
    return render(request, "blogs/blog.html", {"posts": mipost})


def categoria(request, categoria_id):
    """ funcion de categoria """
    micategoria = Categoria.objects.get(id=categoria_id)
    mipost = Post.objects.filter(categorias=micategoria)
    return render(request, "blogs/categoria.html", {"categoria": micategoria, "posts": mipost})
