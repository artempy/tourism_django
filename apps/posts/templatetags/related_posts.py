from django import template
from tagging.models import TaggedItem
from apps.posts.models import Article


register = template.Library()


@register.inclusion_tag('templatetags/related_posts.html')
def related_posts(tags, current_id_article):
    """Get similar articles by any tags from this article"""
    posts = TaggedItem.objects.get_union_by_model(
        Article, tags
    ).exclude(
        pk=current_id_article
    )[:3]

    return {'related_posts': posts}
