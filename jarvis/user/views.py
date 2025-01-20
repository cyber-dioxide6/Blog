from email.message import Message
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from .forms import postform, UserRegistrationForm, ProfileEditForm
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm
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


#Register Section
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_active = False  # Make sure the user is not active until email is verified
            user.save()

            # Send verification email
            token = token_generator.make_token(user)
            uid = urlsafe_base64_encode(str(user.pk).encode('utf-8')) 
            domain = get_current_site(request).domain
            link = f'http://{domain}/activate/{uid}/{token}/'

            subject = "Activate your account"
            message = f"Hi {user.username}!! Click the following link to activate your account: {link}"
            send_mail(subject, message, 'no-reply@yourdomain.com', [user.email])

            return render(request,'registration/sucess_register.html')  # Or redirect to a confirmation page

    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})


#Account Activation Section
def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode('utf-8')
        user = User.objects.get(pk=uid)

        if token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return redirect('login')
        else:
            return HttpResponse("Invalid link")

    except Exception as e:
        return HttpResponse("Error: " + str(e))


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

#View Profile
@login_required
def view_profile(request):
    return render(request, 'view_profile.html', {'user': request.user})

#Edit Profile
@login_required
def edit_profile(request):
    # Ensure UserProfile exists
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile.objects.create(user=request.user)

    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('edit_profile')
    else:
        form = ProfileEditForm(instance=profile)

    return render(request, 'edit_profile.html', {'form': form})


