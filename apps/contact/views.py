from django.shortcuts import render
from apps.contact.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from datetime import datetime


def contact_form(request):
    success = None
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Getting clean fields
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            feedback_email = getattr(settings, 'FEEDBACK_EMAIL')
            recipients = [feedback_email]
            # Get current url of site
            site = request.scheme + '://' +\
                request.META['HTTP_HOST'] + request.path
            date = datetime.now().strftime("%d.%m.%Y в %H:%M")
            # Forming message for send
            message = "{1} написал Вам через форму обратной связи с сайта {0}:\
            \n\n{2}\n\nДата: {3}\
            \nEmail отправителя: {4}".format(site, name, message, date, email)

            try:
                send_mail(subject, message, email, recipients)
            except BadHeaderError:
                raise form.ValidationError('Invalid header found!')
            else:
                success = True

            form = ContactForm()
    else:
        form = ContactForm()

    context_dict = {
        'form': form,
        'success': success
    }

    return render(request, 'contact.html', context_dict)
