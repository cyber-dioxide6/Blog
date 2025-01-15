from email.message import Message
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from .forms import UserRegisterForm, postform
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.
def home(request):
    #Feedback Section form handling
    if request.method =="POST":
        Name = request.POST.get('name')
        Email = request.POST.get('email')
        Feedback = request.POST.get('feedback')
        Date = request.POST.get('date')
        Recommend = request.POST.get('recommend')
        review(name=Name, email=Email ,feedback=Feedback, date=Date, recommend=Recommend).save()
        #Ends here
        return render(request,'user_redirectfeed.html')
    rec = blog.objects.order_by('-date_added')[:9]
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

#Review Confirmation section
def success(request):
    return render(request,'user_redirectfeed.html')


#Aricle Section
@login_required
def articles(request):
    dis = blog.objects.order_by('-date_added')
    return render(request,'articles.html', {'dis': dis})

# Read More Section
def article_detail(request, blog_id):
    article = get_object_or_404(blog, pk=blog_id)
    related_articles = blog.objects.filter(category=article.category).exclude(pk=article.pk)
    return render(request, 'articles_details.html', {'article': article, 'related_articles': related_articles})



# Posts by category View

def category_detail(request, category):
    blogs_in_category= blog.objects.filter(category=category).order_by('-date_added')
    return render(request, 'category_detail.html', {'blogs': blogs_in_category, 'category': category})

#Quiz Section
def quiz(request):
    return render(request,'quiz.html')

def category_list(request):
    categories = Category.objects.all()  # Get all categories with images
    return render(request, 'category_list.html', {'categories': categories})




#Registration Section
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user.setpassword(form.cleaned_data.get['password1'])
            form.save()
            login
            return HttpResponse('User registered successfully')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

#Upload Post Section
@login_required
def upload_post(request):
    if request.method == 'POST':
        form = postform(request.POST, request.FILES)
        if form.is_valid():
            post =form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('articles')
    else:
        form = postform()
    return render(request, 'upload_post.html', {'form': form})