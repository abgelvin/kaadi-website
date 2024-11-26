from django.urls import path
from . import views
from .views import SuccessView
from django.conf import settings


urlpatterns = [
    path('', views.index, name='home'), 
    # path('services/', views.services, name='services'),
    # path('info/', views.info, name='info'), 
    # path('testimonials/', views.testimonials, name='testimonials'),
    # path('contact/', ContactView.as_view(), name='contact'), 
    path('contact/', views.contact_view, name='contact'),
    path('success/', SuccessView.as_view(), name='success'),
    
]


