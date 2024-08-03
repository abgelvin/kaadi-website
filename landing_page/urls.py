from django.urls import path
from . import views
from .views import ContactView, SuccessView

urlpatterns = [
    path('', views.index, name='home'), 
    # path('services/', views.services, name='services'),
    # path('info/', views.info, name='info'), 
    # path('testimonials/', views.testimonials, name='testimonials'),
    path('contact/', ContactView.as_view(), name='contact'), 
    path('success/', SuccessView.as_view(), name='success')
]
