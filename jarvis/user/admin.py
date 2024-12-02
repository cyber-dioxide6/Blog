from django.contrib import admin
from .models import *
# Register your models here.

#Article Registration
@admin.register(blog)
class BlogAdmin(admin.ModelAdmin):
    list_display=('title', 'category', 'date_added')
    list_filter=('category',)

#Review Registration
class reviewAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'email', 'feedback', 'date')
admin.site.register(review, reviewAdmin)

# Contact Registration
class contact_usAdmin(admin.ModelAdmin):
    list_display_contact = ('id', 'username', 'text', 'contact_date')
admin.site.register(contact_us, contact_usAdmin)

#Images
admin.site.register(Category)
