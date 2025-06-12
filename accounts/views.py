from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone

from accounts.forms import RegisterForm, LoginForm, EmailChat, ForgetPasswordForm, DoneForm
from accounts.models import CustomUser, Code
from accounts.utils import  send_html_view
from config import settings


# Create your views here.


def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            password=form.cleaned_data.get('password')
            user=form.save(commit=False)
            print(user,user.password)
            user.set_password(password)
            form.save()
            return redirect("login")
    else:
        form=RegisterForm()
    return render(request, 'accounts/register.html', {'form':form})


def login_view(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect("book:book-list")

    form=LoginForm()
    return render(request,"accounts/login.html",{'form':form})


def logout_view(request):
    logout(request)
    return redirect("login")




def email_chat(request):
    if request.method=='POST':
        form=EmailChat(request.POST)
        if form.is_valid():
            send_mail(
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message'],
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[form.cleaned_data['to']]
            )
            return redirect("book:book-list")

    form=EmailChat()
    return render(request,"accounts/email_chat.html",{'form':form})



def forget_password_view(request):
    if request.method=='POST':
        form=ForgetPasswordForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            user=CustomUser.objects.filter(username=username).first()
            code=Code.objects.create(user=user)
            if user is not None:
                send_html_view(
                    request,
                    subject="Parollingizni o'zgartiring",
                    to_email=user.email,
                    code=code.code,
                    username=user.username
                )
                return render(request,"accounts/done.html",{'form':form})
    form=ForgetPasswordForm()
    return render(request,"accounts/forget_password.html",{'form':form})


def done_view(request):
    username=request.GET.get('name')
    print(username)
    if request.method=='POST':
        form=DoneForm(request.POST)
        if form.is_valid():
            code=form.cleaned_data['code']
            password=form.cleaned_data['password']
            re_password=form.cleaned_data['re_password']
            user = CustomUser.objects.filter(username=username).first()
            if user is not None:
                user_code=Code.objects.filter(user=user,expire_date__gt=timezone.now()).first()
                if code!=user_code.code:
                    print(code,user_code.code,type(user_code.code))
                    return HttpResponse("parol xato yoki mudati otgan")
                if password!=re_password:
                    return HttpResponse("ikki password mos emas")
                user.set_password(password)
                user.save()
                return redirect("login")

    form=DoneForm()
    return render(request,"accounts/reset.html",{'form':form})
