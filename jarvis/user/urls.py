from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('about', views.about),
    path('contact', views.contact),
    path('review', views.review1),
    path('articles', views.articles),
    path('<int:pk>/', views.article_detail, name='article_detail'),
    path('submit',views.success),
    path('contact_submit',views.contact_sucess),
]
