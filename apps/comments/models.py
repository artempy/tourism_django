# -*- coding: utf-8 -*-
from django.db import models
from apps.posts.models import Article
from django.utils import timezone


class Comment(models.Model):
    article_id = models.ForeignKey(Article, verbose_name='Статья')
    author = models.CharField(max_length=64, verbose_name='Автор')
    email_author = models.EmailField(verbose_name='Email адрес')
    text = models.TextField(verbose_name='Комментарий')
    approved = models.BooleanField(verbose_name='Подтвержден?', default=False)
    created_date = models.DateTimeField(verbose_name='Дата комментария',
                                        default=timezone.now)

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'

    def approve(self):
        self.approved = True
        self.save()

    def __str__(self):
        return self.text
