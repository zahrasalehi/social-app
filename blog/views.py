import generics as generics
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Post, Category
from .forms import CostumPostCreationForm


# Create your views here.
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'blog/category_list.html', {'categories': categories})


def category_detail(request, pk):
    category = Category.objects.get(pk=pk)
    return render(request, 'blog/category_detail.html', {'category': category})


def posts(request):
    posts = Post.objects.filter().order_by("-published_date")
    context = {'posts': posts}
    template = loader.get_template('blog/post_list.html')
    return HttpResponse(template.render(context))


def create_posts(request):
    if request.method == "GET":
        return render(
            request, 'blog/createPost.html',
            {"form": CostumPostCreationForm}

        )

    elif request.method == "POST":
        form = CostumPostCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            posts = Post.objects.filter().order_by("-published_date")
            context = {'posts': posts}
            return render(request, 'blog/post_list.html', context)


def post_detial(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
