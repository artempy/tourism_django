from django import template
from apps.posts.models import Article
from tagging.models import TaggedItem


register = template.Library()


@register.inclusion_tag('templatetags/related_posts.html')
def related_posts(tags):
    """Get similar articles by any tags from this article"""
    posts = TaggedItem.objects.get_union_by_model(Article, tags)
    return {'related_posts': posts}
