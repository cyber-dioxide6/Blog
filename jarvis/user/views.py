from email.message import Message
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
# Create your views here.
def home(request):
    rec = blog.objects.order_by('-date_added')[:3]
    recrev = review.objects.order_by('-date')[:6]
    return render(request, 'index.html', {'rec': rec, 'recrev': recrev })


# About Section
def about(request):
    return render(request, 'about.html')



#contact Section

def contact(request):
    if request.method == "POST":
        Username = request.POST.get('username')
        Mail = request.POST.get('mail')
        Text = request.POST.get('text')
        Contact_date = request.POST.get('contact_date')
        contact_us(username=Username, mail=Mail, text=Text, contact_date=Contact_date).save()
        return render(request,'user_redirectcont.html')
    return render(request,'contact.html')

#Contact Confirmation Section 
def contact_sucess(request):
    return render(request,'user_redirectcont.html')

#Review Section
def review1(request):
    if request.method =="POST":
        Name = request.POST.get('name')
        Email = request.POST.get('email')
        Feedback = request.POST.get('feedback')
        Date = request.POST.get('date')
        review(name=Name, email=Email ,feedback=Feedback, date=Date).save()
        return render(request,'user_redirectfeed.html')
    rev = review.objects.all()
        
    return render(request,'review.html',{'rev': rev})

#Review Confirmation section
def success(request):
    return render(request,'user_redirectfeed.html')


#Aricle Section
def articles(request):
    dis = blog.objects.all()
    return render(request,'articles.html', {'dis': dis})

# Read More Section
def article_detail(request, blog_id):
    article = get_object_or_404(blog, pk=blog_id)
    related_articles = blog.objects.filter(category=article.category).exclude(pk=article.pk)
    return render(request, 'articles_details.html', {'article': article, 'related_articles': related_articles})