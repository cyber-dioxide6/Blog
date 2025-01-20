from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.utils import timezone
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


#Articles Section
class blog(models.Model):
    Post_type = [
        ('TECH', 'TECHNOLOGY'),
        ('HTML', 'HTML'),
        ('Tips & Tricks', 'Tips & Tricks'),
        ('CSS', 'CSS'),
        ('Bootstrap', 'BOOTSTRAP'),
        ('Python', 'Python'),
        ('JAVA', 'JAVA'),
        ('JavaScript', 'JavaScript'),
        ('Django', 'Django'),
    ]
    title = models.CharField(max_length=100)
    post = HTMLField(default='')
    image = CloudinaryField('media/image')
    category = models.CharField(max_length=15, choices=Post_type, null=True)
    summary = models.TextField(null=True)
    date_added = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title
# Review Section
class review(models.Model):
    recommendation = [
        ('YES', 'YES'),
        ('NO', 'NO'),
    ]
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50, null=True)
    feedback = models.TextField(null=True)
    date = models.DateField(auto_now_add=True)
    recommend = models.CharField(max_length=3, choices=recommendation, null=True)
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


#Category Images
class Category(models.Model):
    name = models.CharField(choices=blog.Post_type)
    image = CloudinaryField('image', blank=True, null=True)  # Cloudinary image field

    def __str__(self):
        return self.name
    

#User Profile Model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = CloudinaryField('media/image')

    def __str__(self):
        return f"{self.user.username}'s Profile"
    

# Signal to create or update UserProfile
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        instance.userprofile.save()