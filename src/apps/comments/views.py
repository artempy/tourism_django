from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from apps.comments.models import Comment
from apps.comments.forms import CommentForm


def show_comments(request, article, page):
    all_comments = Comment.objects.filter(
        article_id=article
    ).filter(
        approved=True
    ).order_by('-created_date')

    paginator = Paginator(all_comments, 8)

    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)

    return comments


def add_comment(request, article):
    """Helper-function for add comment"""
    success = None
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            success = True
            comment = form.save(commit=False)
            # Setting fields forms for save
            comment.article_id = article
            comment.approved = False
            comment.author = form.cleaned_data['author']
            comment.email_author = form.cleaned_data['email_author']
            comment.text = form.cleaned_data['text']
            comment.save()
            form = CommentForm()
    else:
        form = CommentForm()

    return [form, success]
