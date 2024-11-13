from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    duration = models.IntegerField(blank=True)
    
    def __str__(self):
        return self.description
    

class Testimonial(models.Model):
    client_name = models.CharField(max_length=100, blank=True)
    message = models.TextField()

    def __str__(self):
        return f'{self.message}'
    

class Info(models.Model):
    info_text = models.TextField(blank=True)
    info_image = models.ImageField(blank=True)
    info_video = models.FileField(blank=True)


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

