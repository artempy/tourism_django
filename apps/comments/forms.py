# -*- coding: utf-8 -*-
from django import forms
from apps.comments.models import Comment
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget


class CommentForm(forms.ModelForm):
    """Model's form adding comments"""
    author = forms.CharField(max_length=64, label='Имя')
    email_author = forms.EmailField(label='Email')
    text = forms.CharField(widget=forms.Textarea, label='Комментарий')
    captcha = ReCaptchaField(widget=ReCaptchaWidget(), label='Вы робот?')

    class Meta:
        model = Comment
        fields = ('author', 'email_author', 'text', 'captcha')

    def clean_text(self):
        """Check length of comment"""
        text = self.cleaned_data['text']
        num_words = len(text.split())
        if num_words < 2:
            raise forms.ValidationError('Слишком короткое сообщение!')
        return text
