# -*- coding: utf-8 -*-
from django import forms
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget


class ContactForm(forms.Form):
    name = forms.CharField(max_length=45, label='Ваше имя')
    email = forms.EmailField(label='Email')
    subject = forms.CharField(max_length=40, label='Тема')
    message = forms.CharField(widget=forms.Textarea, label='Сообщение')
    captcha = ReCaptchaField(widget=ReCaptchaWidget(), label='Вы робот?')

    def clean_message(self):
        """Check length of message"""
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError('Слишком короткое сообщение!')
        return message
