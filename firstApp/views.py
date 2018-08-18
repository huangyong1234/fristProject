# _*_ coding: utf-8 _*_
from django.shortcuts import render
from django.http import  HttpResponse
from firstApp import models
import requests

URL_IP = 'http://www.runoob.com/django/django-tutorial.html'

def index(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        models.Article.objects.create(title=username, content=password)
    user_list = models.Article.objects.all()
    return  render(request, 'index.html', {'data':user_list})

def use_simple_requests(request):
    response = requests.get(URL_IP)
    print(">>>>Response Headers:")
    print(response.headers)
    print(">>>>Response Body:")
    print(response.text)
    return render(request, 'test.html', {'responseHeaders':response.headers, 'responseText':response.text})

def use_params_requests(request):
    params = {'parame1':'hello', 'parame2':'world'}
    response = requests.get(URL_IP, params=params)
    print(">>>>Response Headers:")
    print(response.headers)
    print(">>>>Status Code:")
    print(response.status_code)
    print(response.reason)
    print(">>>>Response Body:")
    print(response.json())
    return render(request, 'test.html', {'responseHeaders': response.headers, 'responseText': response.text})