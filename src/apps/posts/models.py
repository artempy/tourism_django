# -*- coding: utf-8 -*-
import re
from django.db import models
from PIL import Image
from django.conf import settings
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.utils.html import strip_tags
from tagging.fields import TagField


class ArticlePageMixin(models.Model):
    slug = models.SlugField(max_length=120, unique=True)
    title_meta = models.CharField(max_length=80, null=True, blank=True)
    description_meta = models.CharField(max_length=150, null=True, blank=True)

    def _get_unique_slug(self):
        if self.slug:
            slug = unique_slug = self.slug
        else:
            slug = unique_slug = slugify(self.name)
        num = 1
        """If slug of article exists in DB then change name's slug"""
        while self.__class__.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def _resize_thumb(self, THUMB_WIDTH=250, THUMB_HEIGHT=180):
        """Create reduced image for article"""
        image = Image.open(self.thumb)
        (width, height) = image.size
        size = (THUMB_WIDTH, THUMB_HEIGHT)
        image = image.resize(size, Image.ANTIALIAS)
        image.save(self.thumb.path)

    def _generate_metatags(self, text, max_length=80):
        text = strip_tags(text)
        if len(text) <= max_length:
            return text
        words = text.split(' ')
        sentences = ''
        for word in words:
            sentences += word + ' '
            if len(sentences) > max_length:
                return sentences.strip()

    def save(self, *args, **kwargs):
        """If slug don't determinated then creating it"""
        id_article = self.__dict__.get('id', None)
        if not self.slug or id_article is None:
            self.slug = self._get_unique_slug()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Category(ArticlePageMixin):
    name = models.CharField(max_length=128,
                            unique=True, verbose_name='Название')
    short_name = models.CharField(max_length=32, blank=True, null=True,
                                  verbose_name='Сокращенное название')
    description = models.TextField(blank=True, null=True,
                                   verbose_name='Описание')
    short_description = models.CharField(max_length=356, blank=True, null=True,
                                         verbose_name='Сокращенное описание')
    thumb = models.ImageField(
        upload_to='images/cat_icon/',
        blank=True,
        null=True,
        verbose_name='Изображение',
        editable=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def save(self, *args, **kwargs):
        """If no set meta-parameters html - title or description then
        generate their"""
        if not self.title_meta:
            self.title_meta = self._generate_metatags(self.name, 55)
        if not self.description_meta:
            self.description_meta = \
                self._generate_metatags(self.description, 100)

        super().save(*args, **kwargs)

        if self.thumb:
            THUMB_WIDTH = getattr(settings, 'THUMB_WIDTH_CAT', 250)
            THUMB_HEIGHT = getattr(settings, 'THUMB_HEIGHT_CAT', 150)
            self._resize_thumb(THUMB_WIDTH, THUMB_HEIGHT)


class Article(ArticlePageMixin):
    category = models.ManyToManyField(Category, verbose_name='Категория')
    name = models.CharField(max_length=128,
                            verbose_name='Название', db_index=True)
    short_post = models.TextField(verbose_name='Краткое описание')
    full_post = models.TextField(verbose_name='Полное описание')
    date = models.DateTimeField(verbose_name='Дата', default=timezone.now)
    slug_cat_unique = models.SlugField(db_index=True, blank=True)
    thumb = models.ImageField(
        upload_to='images/%Y/%m/%d/thumb/',
        blank=True,
        null=True,
        verbose_name='Изображение',
        editable=True)
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

        """If no set meta-parameters html - title or description then
        generate their"""
        if not self.title_meta:
            self.title_meta = self._generate_metatags(self.name, 55)
        if not self.description_meta:
            self.description_meta = \
                self._generate_metatags(self.full_post, 100)

        super().save(*args, **kwargs)
        """Resize image"""
        if self.thumb:
            THUMB_WIDTH = getattr(settings, 'THUMB_WIDTH', 150)
            THUMB_HEIGHT = getattr(settings, 'THUMB_HEIGHT', 225)
            self._resize_thumb(THUMB_WIDTH, THUMB_HEIGHT)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
