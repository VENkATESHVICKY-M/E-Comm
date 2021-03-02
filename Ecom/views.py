from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product
from django.contrib.auth.models import User,auth

# Create your views here.
def store(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request ,'store.html' , context)

def signup(request):
    if request.method == 'POST':
        username=request.POST['username']
        lastname=request.POST['lastname']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1 == password2:
            user = User.objects.create_user(username=username,password=password1,last_name=lastname,email=email)
            user.save()
            print("created")
            return redirect('/login')
        else:
            context = {'msg' : 'incorrectpassword'}
            return render(request ,'signup.html' , context)
    else:
        return render(request ,'signup.html' )

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            context = {'msg' : 'Invalid UserID and Password'}
            return render(request ,'login.html' , context)
    else:
        return render(request ,'login.html' )


def cart(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request ,'cart.html' , context)

def logout(request):
    auth.logout(request)
    return redirect('/')

