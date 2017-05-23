import operator
from functools import reduce
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.views.generic.list import ListView
from django.db.models import Q
from apps.posts.models import Category, Article
from apps.comments.views import show_comments, add_comment


def index(request):
    categories = Category.objects.all().order_by('name')
    for category in categories:
        # IF p tag occur in text then get first paragraph
        if '</p>' in category.description:
            category.description = category.description.split("</p>")[0]\
                .replace('<p>', '')
    return render(request, 'index.html', {'categories': categories})


def search(request):
    if request.method == 'POST':
        query = request.POST.get('q')
        if query:
            query_list = query.split()
            results = Article.objects.filter(
                reduce(operator.and_, (Q(name__icontains=q)
                                       for q in query_list)
                       )
            )[:15]
            return render(request, 'search_results.html',
                          {'results': results, 'query': query})
    return redirect(reverse('index'))


class ShowCat(ListView):
    model = Article
    http_method_names = ['get']
    context_object_name = 'posts'
    template_name = 'category.html'
    paginate_by = 10

    def dispatch(self, request, *args, **kwargs):
        cat_slug = kwargs.get('category_slug', None)
        self.cat = get_object_or_404(Category, slug=cat_slug)
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Article.objects.filter(category=self.cat).order_by('-date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_meta'] = self.cat.title_meta
        context['description_meta'] = self.cat.description_meta
        context['category'] = self.cat
        context['starturl'] = reverse('category', args=[self.cat.slug])

        return context


def show_article(request, category_slug, article_slug, page=None):
    success = None
    cat = get_object_or_404(Category, slug=category_slug)
    article = get_object_or_404(Article, slug=article_slug)

    # Getting comments for current article
    comments = show_comments(request, article, page)

    # Getting form add comment and status
    form, success = add_comment(request, article)

    context_dict = {
        'title_meta': "%s / %s " % (article.title_meta, cat.name),
        'description_meta': article.description_meta,
        'category': cat,
        'article': article,
        'form': form,
        'success': success,
        'comments': comments,
        'starturl': reverse('article', args=[cat.slug, article_slug])
    }

    return render(request, 'article.html', context_dict)
