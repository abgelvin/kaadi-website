from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.views.generic import TemplateView, FormView
from .forms import ContactForm
import logging

logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'landing_page/index.html')


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

def contact_view(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            subject = form.cleaned_data.get('subject')
            message = f'You have a message from {name}: {form.cleaned_data.get("message")}'
            print(f'message: {message}')
            print('sending email...')
            try:
                send_mail(
                subject,
                message,
                email,
                ['abgelvin@gmail.com'],
                fail_silently=False
                )
                print(f'mail sent')
            except Exception as e:
                logger.error(f'error sending email: {e}')
            # messages.success(request, 'success')
            # EmailMessage(
            #     subject,
            #     f'Email from {name}: {message}',
            #     email,
            #     ['abgelvin@gmail.com']
            # ).send()
            return redirect('success')
        else:
            logger.error('form is invalid')
            logger.error(form.errors)
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

# def success(request):
#     return 
            
    

# def send_email(request):
#     send_mail(subject=request.POST.get('subject'),
#               from_email=request.POST.get('email'),
#               message=request.POST.get('message'),
#               recipient_list='abgelvin@gmail.com')
#     return reverse('success')