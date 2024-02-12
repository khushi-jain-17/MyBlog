from django.shortcuts import render,redirect 
from django.contrib.auth import authenticate,login,logout 
from django.contrib import messages
from .forms import SignUpForm
from .models import Post 

def index(request):
    posts=Post.objects.all()
    return render(request,'index.html',{ 'posts':posts })

def post(request,pk):
    posts=Post.objects.get(id=pk)
    return render(request,'posts.html',{'posts':posts})


def register_user(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,'You have been Succesfully registered! welcome')
            return redirect('login')
    else:
        form= SignUpForm()
        return render(request,'register.html',{'form':form}) 
    return render(request,'register.html',{'form':form})   
    
def login_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have been logged in")
            return redirect('index')
        else:
            messages.success(request,"There was an Error logging in,Please try again...")
            return redirect('login')
    else:      
        return render(request,'login.html')

def logout_user(request):
    logout(request)
    return redirect('login')





