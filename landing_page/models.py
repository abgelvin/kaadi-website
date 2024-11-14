from django.db import models


class Service(models.Model):
    text = models.TextField()


class Session(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='uploads/', blank=True)
    image_url = models.URLField(blank=True)
    
    def get_image(self):
        if self.image:
            return self.image.url
        return self.image_url
    
    def __str__(self):
        return 'Session description text'
    

class Approach(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='uploads/', blank=True)
    image_url = models.URLField(blank=True)

    def get_image(self):
        if self.image:
            return self.image.url
        return self.image_url
    
    def __str__(self):
        return 'My approach text'


class About(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='uploads/', blank=True)
    image_url = models.URLField(blank=True)

    def get_image(self):
        if self.image:
            return self.image.url
        return self.image_url
    
    def __str__(self):
        return 'About me text'


class Testimonial(models.Model):
    client_name = models.CharField(max_length=100, blank=True)
    message = models.TextField()

    def __str__(self):
        return f'{self.message}'
    

class Info(models.Model):
    title = models.CharField(max_length=100, blank=True)
    text = models.TextField(max_length=500)
    image = models.ImageField(upload_to='uploads/', blank=True)
    image_url = models.URLField(blank=True)
    video = models.FileField(blank=True)

    def get_image(self):
        if self.image:
            return self.image.url
        return self.image_url
    
    def __str__(self):
        return f'{self.info_title}'


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

