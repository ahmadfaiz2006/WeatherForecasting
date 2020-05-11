from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello")

def weather(request):
    
    return render(request,"index.html")

def weatherpage(request):
    x = request.GET.get("weathercity","default")
    import requests
    import json
    try:
        url = "http://api.openweathermap.org/data/2.5/weather?appid=3c1f3dc53ab8e97b8ce559caa976b58e&q="+str(x)
        api_requests = requests.get(url).json()
    except Exception as e:
        api = "Error..."
    # temperature = api["main"][0]
    # temperature = (temperature – 32) * 5/9
    params = {'x':api_requests, 'name':x.title()}
    return render(request,"weatherpage.html",params)

def back(request):
    return render(request,"index.html")
