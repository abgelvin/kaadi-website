from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage, get_connection
from django.conf import settings
from django.views.generic import TemplateView, FormView
from .forms import ContactForm
import logging
from .models import Info, Testimonial, Service

logger = logging.getLogger(__name__)


def index(request):
    info = Info.objects.all()
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()
    context = {
        'info': info,
        'services': services,
        'testimonials': testimonials
    }

    return render(request, 'landing_page/index.html', context)


# def info_view(request):
#     pass


# def testimonial_view(request):
#     pass


# def contact(request):
#     pass


class SuccessView(TemplateView):
    template_name = 'success.html'


# class ContactView(FormView):
#     form_class = ContactForm
#     template_name = 'contact.html'
#     success_url = '/success/'    
        

#     def form_valid(self, form):
#         name = form.cleaned_data.get('name')
#         email = form.cleaned_data.get('email')
#         message = form.cleaned_data.get('message')
#         summary = f'{name} @ {email} said: {message}'
#         subject = form.cleaned_data.get('subject')
#         send_mail(
#             subject=subject,
#             message=summary,
#             from_email=email,
#             recipient_list=['abgelvin@gmail.com']
#         )

#         return super(ContactView, self).form_valid(form)


# def send_mail(request):
#     form = ContactForm()
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data.get('name')
#             # email = form.cleaned_data.get('email')
#             subject = form.cleaned_data.get('subject')
#             message = f'You have a message from {name}: {form.cleaned_data.get("message")}'
#             print(f'message: {message}')
#             print('sending email...')
#             try:
#                 with get_connection(
#                     host=settings.EMAIL_HOST,
#                     port=settings.EMAIL_PORT,
#                     username=settings.EMAIL_HOST_USER,
#                     password=settings.EMAIL_HOST_PASSWORD,
#                     use_tls=settings.EMAIL_USE_TLS
#                 ) as connection:
#                     subject = request.POST.get('subject')
#                     email_from = settings.EMAIL_HOST_USER
#                     recipient_list = [settings.EMAIL_HOST_USER]
#                     message = request.POST.get('message')
#                     EmailMessage(subject, message, email_from, recipient_list, connection=connection).send()

#                 return render(request, 'success.html')
#             except Exception as e:
#                 logger.error(f'error sending email: {e}')
#     else:
#         form = ContactForm()
#     return render(request, 'contact.html', {'form': form})


def contact_view(request):
    """GET displays contact form or POST sends email from contact form"""

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            subject = form.cleaned_data.get('subject')
            message = f'You have a message from {name} @ {email}: \n{form.cleaned_data.get("message")}'
            print(f'message: {message}')
            print('sending email...')
            try:
                print('trying')
                send_mail(
                    subject,
                    message,
                    'kaadilove@hotmail.com',
                    ['abgelvin@gmail.com'],
                )
                print(f'mail sent')
            except Exception as e:
                logger.error(f'error sending email: {e}')
            return redirect('success')
        else:
            logger.error('form is invalid')
            logger.error(form.errors)
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
