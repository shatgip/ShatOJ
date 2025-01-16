from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect
from accounts.models import CustomUser
from django.contrib import messages

def index(request):
    username = request.GET.get('username')
    return render(request, 'index.html',{'username':username})

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if CustomUser.objects.filter(username=username).exists():
            return render(request, 'accounts/register.html',{'error_text':'用户名已存在，请重新输入'})
        user = CustomUser()
        user.username = username
        user.password = password
        user.save()
    return render(request,'accounts/register.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, '登录成功')
            is_logged_in=True
            return render(request, 'index.html',{'is_logged_in':is_logged_in,'username':username})
        else:
            is_logged_in=False
            return render(request, 'accounts/login.html', {'error_text':'用户名或密码输入错误','is_logged_in': is_logged_in})
    return render(request, 'accounts/login.html')

def logout(request):
    auth_logout(request)
    return redirect('login')