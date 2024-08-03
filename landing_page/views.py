from django.shortcuts import render
from django.urls import reverse
from django.core.mail import send_mail
from django.views.generic import TemplateView, FormView
from .forms import ContactForm


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


class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contact.html'


    def get_success_url(self):
        return reverse('success')
    

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        subject = form.cleaned_data.get('subject')
        message = form.cleaned_data.get('message')

        return super(ContactView, self).form_valid(form)
    