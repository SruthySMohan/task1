from django.shortcuts import render

# Create your views here.
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
# from .models import Branches
from .models import Form


def home(request):

     return render(request,'home.html')
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['conform_password']
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Id already exists")

                return redirect('register')

            else:
             user=User.objects.create_user(username=username,email=email,password=password)

             user.save()
             return redirect('login')

        else:
            messages.info(request,"Password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            # return redirect('/')
            return redirect('reg_form')

        else:
            messages.info(request,"Invalid Credentials")
            return redirect('login')
    return render(request,'login.html')

def reg_form(request):
    return render(request,'reg_form.html')
def form(request):
    if request.method=='POST':
        # name = request.POST.get('name')
        dob= request.POST.get('dob')
        gender = request.POST.get('gender')
        number = request.POST.get('number')
        email = request.POST.get('email')
        address = request.POST.get('address')
        # district = request.POST.get('district', )
        # branches = request.POST.get('branches', )
        # account = request.POST.get('account', )
        # var= Form(dob=dob,gender=gender,number=number,
        #              email=email,address=address)



        # if name is None:
        #     print("empty")
        # if var is None:
        #     messages.info(request, "field empty")
        # else:
        # var.save()
        return redirect('submit')
    return render(request,'form.html')

def reg1(request):
    if request.method=='POST':
    #     name = request.POST.get('name', )
    #     dob= request.POST.get('dob', )
    #     gender = request.POST.get('gender', )
    #     number = request.POST.get('number', )
    #     email = request.POST.get('email', )
    #     address = request.POST.get('address', )
    #     district = request.POST.get('district', )
    #     branches = request.POST.get('branches', )
    #     account = request.POST.get('account', )
    #     var= Form(name=name,dob=dob,gender=gender,number=number,
    #                  email=email,address=address,district=district,
    #                  branches=branches,account=account)
    #     if var is  None:
    #         messages.info(request, "field empty")
    #     else:
    #         var.save()
         return redirect('submit')

    return render(request,'form.html')
def submit(request):
    return render(request,'submit.html')
def logout(request):
    auth.logout(request)
    return redirect('/')