from django.shortcuts import render
from django.http import HttpResponse
from .models import blogpost
# Create your views here.

def index(request):
    allpost = blogpost.objects.all()
    print(allpost)
    params = {'allpost': allpost}
    return render(request,'blog\index.html',params)

def Blogpost(request,id):
    post = blogpost.objects.filter(post_id=id)[0]
    print(post)
    return render(request,'blog\\blogpost.html',{'post':post})