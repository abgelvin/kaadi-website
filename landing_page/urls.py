from django.urls import path

urlpatterns = [
    path('', views.home, name='home'), 
    path('services/', views.sevices, name='services'),
    path('info/', views.info, name='info'), 
    path('testimonials/', views.testimonials, name='testimonials'),
    path('contact/', views.contact, name='contact')
]
