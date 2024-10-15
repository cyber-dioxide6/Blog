from django.db import models
from django.utils import timezone
# Create your models here.


#Articles Section
class blog(models.Model):
    Post_type = [
        ('TECH', 'TECHNOLOGY'),
        ('AI', 'ARTIFICIAL INTELLIGENCE'),
        ('ML', 'MACHINE LEARNING'),
        ('IOT', 'INTERNET OF THINGS'),
        ('AUTO', 'AUTOMATIONS'),
    ]
    title = models.CharField(max_length=100)
    post = models.TextField(max_length=1000)
    image = models.ImageField(upload_to= 'media')
    cate = models.CharField(max_length=5, choices=Post_type, null=True)
    date_added = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title
# Review Section
class review(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50, null=True)
    feedback = models.TextField(null=True)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name

# Contact Section

class contact_us(models.Model):
    username = models.CharField(max_length=20, null=True)
    mail = models.EmailField(max_length=30, null=True)
    text = models.TextField(max_length=50, null=True)
    contact_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.username
