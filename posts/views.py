from django.shortcuts import redirect, render,get_object_or_404
from django.core.mail import send_mail
from django.core.mail import EmailMessage
# from posts.forms import addPostForm
from . models import *
#from multiprocessing import context
from django.shortcuts import get_object_or_404, render, redirect
#from django.contrib import messages
from .models import Poster
from .forms import AddPostForm
#import os

def hello(request):
    return render(request, 'posts/hello.html')

# def show_post(request,post_id):
#     post=get_object_or_404(Mosts, pk=post_id)
#     context={'post':post}
#     return render(request,'posts/post.html',context=context)
    
# def show_post(request,post_slug):
#     post=get_object_or_404(Tosts, slug=post_slug)
#     context={'post':post}
#     return render(request,'posts/post.html',context=context)
        
def send_message(request):
    # send_mail("Web programming","My content",
    #            "200103157@stu.sdu.edu.kz",
    #            ["200103157@stu.sdu.edu.kz","200103231@stu.sdu.edu.kz","200103503@stu.sdu.edu.kz","200103082@stu.sdu.edu.kz"],
    #            fail_silently=False, html_message="<b>You are beautiful</b>")
    # return render(request,'posts/hello.html')

    email=EmailMessage("Hello","body",
              "200103157@stu.sdu.edu.kz",
              ["kezhanna.03@mail.ru","200103157@stu.sdu.edu.kz"],
              headers={'Message-ID':'foo'},)
    email.attach_file('C:/Users/Жанна/Desktop/100APPLE/tort.JPG')
    email.send(fail_silently=False)
    return render(request,'posts/hello.html')              
def getarea(radius):
    return 3.14*radius*radius


def registration(request):
    file_data=request.FILES
    if request.method=='POST':
        form=AddPostForm(request.POST,file_data)
        # print(request.POST)
        if form.is_valid():
            #print(form.cleaned_data)
            try:
                #form.save()
                Poster.objects.create(**form.cleaned_data)
                return redirect('show_post')
            except:
                form.add_error(None,'Paidalanuwyny koskanda kate wykty.')
    else:
        form=AddPostForm()
    return render(request,'posts/registration.html', {'title':'Paidalanuwy kosu','form':form})

def show_post(request):
    post=Poster.objects.all().order_by('-id')[:1]
    context={'post':post}
    return render(request,'posts/post.html', context=context)

