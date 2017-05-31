from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
from apps.posts.models import Category, Article


class CategorySitemap(Sitemap):
    changefreq = 'monthly'
    priority = '0.9'

    def items(self):
        return list(Category.objects.all())

    def location(self, obj):
        return '/{}/'.format(obj.slug)


class ArticleSitemap(Sitemap):
    changefreq = 'monthly'
    priority = '0.8'

    def items(self):
        return list(Article.objects.all())

    def location(self, obj):
        return '/{0}/{1}.html'.format(obj.slug_cat_unique, obj.slug)

    def lastmod(self, obj):
        return obj.date


class StaticSitemap(Sitemap):
    def __init__(self, names, change_frequency, priority):
        self.names = names
        self.changefreq = change_frequency
        self.priority = priority

    def items(self):
        return self.names

    def location(self, obj):
        return reverse(obj)


SITEMAPS = {
    'dynamic': StaticSitemap(
        [
            'index',
        ],
        'weekly', '1.0'),
    'category': CategorySitemap,
    'article': ArticleSitemap,
}
