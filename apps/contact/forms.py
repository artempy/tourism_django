# -*- coding: utf-8 -*-
from django import forms
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=64, label='Ваше имя',
                           help_text='Введите ваше имя')
    email = forms.EmailField(label='Email', help_text='Введите ваш Email')
    message = forms.CharField(widget=forms.Textarea, label='Текст')
    captcha = ReCaptchaField(widget=ReCaptchaWidget())
    #datetime.now().strftime("%d.%m.%y в %H:%M")

    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError('Слишком короткое сообщение!')
        return message
