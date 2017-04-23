from django import template
from apps.posts.models import Article


register = template.Library()


@register.inclusion_tag('templatetags/top_articles.html')
def get_top_articles():
    """Get similar articles by any tags from this article"""
    try:
        posts = Article.objects.all().order_by('-likes')[:7]
    except Article.DoesNotExist:
        posts = None
    return {'top_articles': posts}
