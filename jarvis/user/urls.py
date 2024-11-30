from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('review/', views.review1,name='review'),
    path('articles/', views.articles,name='articles'),
     path('articles/<int:blog_id>/', views.article_detail, name='article_detail'),
    path('submit/',views.success),
    path('contact_submit/',views.contact_sucess),
]
