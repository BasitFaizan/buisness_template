from django.contrib import messages
from django.shortcuts import redirect, render,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
    return render(request, 'website/index.html')

def signUp(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cPassword = request.POST.get('cPassword')
        print(f"{username} {email} {password}")
        if password != cPassword:
            messages.warning(request,'passwords do not match!')
            return redirect('signUp')
        elif User.objects.filter(username=username).exists():
            messages.error(request,'Username already taken! try another one.')
            return redirect('signUp')
        else:
            myuser = User.objects.create_user(username,email,password=password)
            myuser.save()
            return redirect('logIn')
    return render(request,"website/sign.html")

def log_in(request):
    if request.method == "POST":
        usernmae  = request.POST.get('username')
        passwrd   = request.POST.get('password')
        print(f"{usernmae} {passwrd}")

        user= authenticate(username=usernmae , password=passwrd )
        print('login')
        if user:
            login(request,user)
            return redirect('/')
    return render(request,"website/login.html")
def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')