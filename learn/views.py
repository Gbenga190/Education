from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserForm, user_profileForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from . models import SubscribedUsers
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib  import messages
from django.core.mail import EmailMessage

# Create your views here.

def index(request):
    return render(request,'learn/index.html')

def about(request):
    return render(request,'learn/about.html')

def blog(request):
    return render(request,'learn/blog.html')

def programming_language(request):
    return render(request,'learn/language.html')

def artificial_intelligence(request):
    return render(request,'learn/artificial_intelligence.html')

def business_proposal(request):
    return render(request,'learn/business_proposal.html')

def cyber_security(request):
    return render(request,'learn/cyber_security.html')
    
def register(request):

    registered = False

    if request.method== 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = user_profileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form =UserForm()
        profile_form = user_profileForm()

    context = {
        'registered':registered,
        'user_form':user_form,
        'profile_form':profile_form,
    }
    return render (request, 'learn/register.html', context)


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('ACCOUNT IS DEACTIVATED')

        else:
            return HttpResponse('Please use correct id and password')
    else:
        return render(request, 'learn/login.html')


# Login required'
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email', None)

        if not email:
            messages.error(request, "You must type  legit email to subscribe to our Newsletter")
            return redirect("/")


        subscribe_user = SubscribedUsers.objects.filter(email=email).first()
        if subscribe_user:
            messages.error(request, f"{email} email address is already subscriber.")
            return redirect(request.META.get("HTTP_REFERER", "/"))  

        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request, e.messages[0])
            return redirect("/")

        subscribe_model_instance = SubscribedUsers()
        subscribe_model_instance.email = email
        subscribe_model_instance.save()
        messages.success(request, f'{email} email has successfully subscribed to our newsletter!')
        return redirect(request.META.get("HTTP_REFERER", "/"))