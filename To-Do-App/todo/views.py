from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from todo import models
from todo.models import ToDoo
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth .decorators import login_required


def signup(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        emailid = request.POST.get('email')
        pwd = request.POST.get('pwd')

        #  Check if username already exists
        if User.objects.filter(username=fnm).exists():
            messages.error(request, "Username already taken! Please choose another one.")
            return redirect('signuppage')

        #  Create new user
        my_user = User.objects.create_user(fnm, emailid, pwd)
        my_user.save()
        messages.success(request, "Account created successfully! Please login.")
        return redirect('/login')

    return render(request, 'sign.html')

def login_view(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        pwd = request.POST.get('pwd')
        print(fnm, pwd)
        
        user = authenticate(request, username=fnm, password=pwd)
        if user is not None:
           
            login(request, user)
            return redirect('/todopage')
        else:
            return redirect('/login')

    return render(request, 'login.html')
@login_required(login_url='/login')
def todopage(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        
        obj = models.ToDoo(title=title, user=request.user)
        obj.save()
        return redirect('/todopage')   # Redirect after save

    # GET request — show todos
    res = models. ToDoo.objects.filter(user=request.user).order_by('-data')
    return render(request, 'todo.html', {'res': res})
@login_required(login_url='/login')
def edit_todo(request,sr_no):
    obj = models.ToDoo.objects.get(sr_no=sr_no)
    if request.method == 'POST':
        title = request.POST.get('title')
        
        obj.title=title
        obj.save()
        return redirect('/todopage')  
   
    # GET request — show todos
    res = models.ToDoo.objects.filter(user=request.user).order_by('-data')
    return render(request, 'edit_todo.html', {'res': res,'edit_obj':obj})
@login_required(login_url='/login')
def delete_todo(request,sr_no):
    obj =models.ToDoo.objects.get(sr_no=sr_no)
    obj.delete()
    return redirect('/todopage')

def signout(request):
    logout(request)
    return redirect('/login')

    





