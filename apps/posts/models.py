# -*- coding: utf-8 -*-
import re
from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from tagging.fields import TagField


class ArticlePageMixin(models.Model):
    slug = models.SlugField(unique=True)
    title_meta = models.CharField(max_length=80, null=True, blank=True)
    description_meta = models.CharField(max_length=150, null=True, blank=True)

    def _get_unique_slug(self):
        slug = unique_slug = slugify(self.name)
        num = 1
        """If slug of article exists in DB then change name's slug"""
        while self.__class__.__name__.objects.\
                filter(slug=unique_slug).exists():
            unique_slug = '{1}-{2}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        """If slug don't determinated then creating it"""
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Category(ArticlePageMixin):
    name = models.CharField(max_length=128,
                            unique=True, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    icon = models.URLField(null=True, blank=True,
                           verbose_name='Адрес к иконке')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Article(ArticlePageMixin):
    category = models.ManyToManyField(Category, verbose_name='Категория')
    prefix_slug = models.SlugField(blank=True)
    name = models.CharField(max_length=128,
                            verbose_name='Название', db_index=True)
    short_post = models.TextField(verbose_name='Краткое описание')
    full_post = models.TextField(verbose_name='Полное описание')
    date = models.DateTimeField(verbose_name='Дата', default=timezone.now)
    thumb = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True,
                              null=True, verbose_name='Изображение')
    tags = TagField(blank=True)
    likes = models.IntegerField(default=0, db_index=True, blank=True)

    def _create_tags(self):
        """Create tags from name of article"""
        words = re.split('\W+', self.name)
        words = list(filter(lambda word: len(word) > 3, words))
        return " ".join(words).lower()

    def save(self, *args, **kwargs):
        """If tags not determinated then generating their"""
        if not self.tags:
            tags = self._create_tags()
            if tags:
                self.tags = self._create_tags()

        if not self.prefix_slug:
            pass
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
