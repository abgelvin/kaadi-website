from django.db import models
from . import views


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    duration = models.DurationField()

    def __str__(self):
        return self.name
    

class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f'{self.message} - {self.client_name}'
    

class Info(models.Model):
    question = models.CharField(max_length=200)
    answer_text = models.TextField()
    answer_video = models.FileField()


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

