from django.shortcuts import render
from .forms import userform,app,Postss
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from jobpostapp.models import jobpost,job,post
from django.views.generic import ListView,DetailView,CreateView

# Create your views here.
def register(request):
    submit = False
    if request.method == 'POST':
        print("hi")
        form = userform(request.POST)
        print(form)
        if form.is_valid():
            print("success")
            user = form.save()
            user.save()
            submit =True
            print("username :",form.cleaned_data.get("username"))
            print("password1 :",form.cleaned_data.get("password1"))

        else:
            return HttpResponse("Data was not saved please try again")
            
    else:
        form =userform()
    return render(request,"register.html",{"form":form,"submit":submit})



def index(request):
    prema = post.objects.all()
    print(prema)
    return render(request,"home.html",{'form':prema})

def user_login(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password =request.POST.get('password')

        user= authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return redirect('home')
            else:
                return HttpResponse(" please check your creds")
        
        else:
            return HttpResponse("please check your creds")
        
    return render(request,"login.html",{})


def home(request):
    nara = post.objects.all()
    print(nara)
    return render(request,"home.html",{'form':nara})

def user_logout(request):

    logout(request)
    return redirect('user_login')


def apply(request):
    register = False
    form = app()
   
    if request.method == 'POST':
        form = app(request.POST)
        if form.is_valid():
            form.save()
            register = True
            print("application successfully submited")
    return render(request,"jobpost/job.html",{'form':form,'register':register})


def dash(request):
    form = job.objects.all()
    return render(request,"jobpost/dash.html",{'form':form}) 



def Apply(request):
    simha = job.objects.all()
    return render(request,"jobpost/applied.html",{'simha':simha})


def addpost(request):
    form = Postss()
    if request.method == 'POST':
        form = Postss(request.POST,request.FILES)
        if form.is_valid():
         form.save()
         print("form added successfull")
         return redirect('home')
    return render(request,"jobpost/add_post.html",{'form':form})


def blog(request):
    java = post.objects.all()
    return render(request,"blog.html",{'java':java})