from django.shortcuts import render,redirect
from home.forms import ProfileForm,infoprofileform
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout,login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from home.models import Details
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,"index.html")

def regi(request):
    form = UserCreationForm
    if request.method == "POST":
        regForm=UserCreationForm(request.POST)
        if regForm.is_valid():
            regForm.save()
            messages.success(request,'USER HAS BEEN REGISTERED')
    return render(request,"registration.html",{'form':form})
def profile_reg(request):
    register=False
    if request.method=="POST":
        profile_form=ProfileForm(data=request.POST)
        info_form=infoprofileform(data=request.POST)

        if profile_form.is_valid() and info_form.is_valid():
            user=profile_form.save()
            user.save()
            profile=info_form.save(commit=False)
            profile.user=user
            profile.save()
            register=True
        else:
            HttpResponse("<h2>Something Went Wrong With The Form.</h2>")
    else:
        profile_form = ProfileForm(data=request.POST)
        info_form = infoprofileform(data=request.POST)
    return render(request,'Register.html',{
                            'profile_form':profile_form,
                            'info_form':info_form,
                            'register':register
        })

def loginuser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/fillup")
        else:
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutuser(request):
    logout(request)
    return redirect("/login")

def fillup(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        quantity=request.POST.get('quantity')
        country=request.POST.get('country')
        city=request.POST.get('city')
        Dcountry=request.POST.get('Dcountry')
        Dcity=request.POST.get('Dcity')
        details=Details(name=name,email=email,quantity=quantity,country=country,city=city,Dcountry=Dcountry,Dcity=Dcity)
        details.save()
        messages.success(request, 'Your details have been successfully updated!!!')

    return render(request,"fillup.html")