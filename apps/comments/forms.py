# -*- coding: utf-8 -*-
from django import forms
from django.utils import timezone
from apps.comments.models import Comment
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget


class CommentForm(forms.ModelForm):
    """Model's form adding comments"""
    author = forms.CharField(max_length=64, label='Имя',
                             help_text='Пожалуйста, введите ваше имя')
    email_author = forms.EmailField(label='Email',
                                    help_text='Введите ваш email')
    text = forms.CharField(widget=forms.Textarea, label='Комментарий',
                           help_text='Пожалуйста, введите ваш комментарий')
    captcha = ReCaptchaField(widget=ReCaptchaWidget())
    article = forms.CharField(widget=forms.HiddenInput())
    created_date = forms.DateTimeField(initial=timezone.now)
    approved = forms.BooleanField(initial=False)

    class Meta:
        model = Comment
        fields = ('author', 'email_author', 'text', 'captcha')
