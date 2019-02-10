from django.shortcuts import render, redirect
from django.http import HttpResponse
import urllib.parse
import json
import requests
from .models import Hospitals

# Create your views here.
def register(request):
    if request.method=='POST':
        address = request.POST['address']
        name = request.POST['name']
        files = request.FILES['files']
        x=address.replace(" ","%20")
        response = requests.get('https://apis.mapmyindia.com/advancedmaps/v1/jx3b1373lb88adhz5lhzzwiof2fikpsg/geo_code?addr='+x)
        json_data = json.loads(response.text)
        lat = json_data['results'][0]['lat']
        lng = json_data['results'][0]['lng']
        f_add = json_data['results'][0]['formatted_address']
        hospitals = Hospitals()
        hospitals.address = f_add
        hospitals.name = name
        hospitals.files = files
        hospitals.lat = lat
        hospitals.lng = lng
        hospitals.save()
        print(response)
        context = {'lat':lat, 'lng':lng, 'f_add':f_add}
        return render(request, 'hospitals/register.html', context)
    else:
        return render(request, 'hospitals/register.html')

def map(request):
    return render(request, 'hospitals/map.html')


def index(request):
    return render(request, 'hospitals/index.html')

def about(request):
    return render(request, 'hospitals/about.html')

def feedback(request):
    return render(request, 'hospitals/feedback.html')