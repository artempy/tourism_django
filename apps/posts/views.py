from django.shortcuts import render, get_object_or_404
from apps.posts.models import Category, Article


def index(request):
    return render(request, 'index.html', {})


def search(request):
    return render(request, 'index.html', {})


def show_cat(request, category_slug):
    context_dict = {}
    cat = get_object_or_404(Category, slug=category_slug)
    posts = Article.objects.filter(category=cat)
    context_dict['title_meta'] = cat.title_meta
    context_dict['description_meta'] = cat.description_meta
    context_dict['category'] = cat
    context_dict['posts'] = posts
    return render(request, 'category.html', context_dict)


def show_article(request, category_slug, article_slug):
    print(category_slug, article_slug)
    context_dict = {}
    cat = get_object_or_404(Category, slug=category_slug)
    article = get_object_or_404(Article, slug=article_slug)
    print(article)
    context_dict['title_meta'] = article.title_meta
    context_dict['description_meta'] = article.description_meta
    context_dict['category'] = cat
    context_dict['article'] = article
    return render(request, 'article.html', context_dict)
