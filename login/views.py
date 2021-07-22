from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

def index (request):

    return render(request, 'index.html')
def login (request):
    if request.method=="POST":
        name=request.POST['name']
        pass1=request.POST['password']
        user=auth.authenticate(username=name,password=pass1)
        if user is not None:
            auth.login(request,user)
            messages.info(request,"welcome user:")

            return redirect('/#section2')
        else:
            messages.info(request,"Invalid credential")
            return redirect('/#section2')
    else:
        return  render(request,'index.html')

def register (request):

    if request.method=="POST":
        name1=request.POST['name']
        print(name1)
        email=request.POST['email']
        pass1=request.POST['password']
        pass2=request.POST['repassword']

        if pass1==pass2:
            if User.objects.filter(username=name1).exists():
                messages.info(request,"Username already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email is already taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=name1, email=email, password=pass1)
                user.save();
                messages.info(request,"User is created")
        else:
            messages.info(request,"password don't match")
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'index.html')