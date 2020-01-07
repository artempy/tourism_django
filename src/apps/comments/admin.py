from django.contrib import admin
from apps.comments.models import Comment


def make_approve(modeladmin, request, queryset):
    queryset.update(approved=True)


make_approve.short_description = 'Одобрить выбранные комментарии'


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'article_id',
        'author',
        'text',
        'approved',
        'created_date'
    )
    fields = (
        'article_id',
        'author',
        'email_author',
        'text',
        'approved',
        'created_date'
    )
    list_filter = ['created_date']
    ordering = ('approved', '-created_date',)
    date_hierarchy = 'created_date'
    actions = [make_approve]


admin.site.register(Comment, CommentAdmin)
