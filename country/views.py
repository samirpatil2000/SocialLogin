from django.shortcuts import render,redirect
from django.http import HttpResponse
from country.models import country
from .forms import countryForm
from django.contrib.auth.decorators import login_required
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import country
from .serializers import CountrySerializer

# Create your views here.
@login_required(login_url="/account/login/")
def index(request):
    country_list = country.objects.all()
    context ={
        'country_list':country_list
    }
    return render(request,'country/index2.html',context)

@login_required(login_url="/account/login/")
def details(request,country_id):
    countrys = country.objects.get(id=country_id)
    return render(request,'country/details.html',{'country':countrys})

@login_required(login_url="/account/login/")
def add_country(request):
    if request.method == "POST":
        country_name=request.POST.get('country_name',)
        currency=request.POST.get('currency',)
        country_image=request.FILES['country_image']
        native_name=request.POST.get('native_name',)
        capital=request.POST.get('capital',)
        population=request.POST.get('population',)
        country_code=request.POST.get('country_code',)
        laguage=request.POST.get('laguage',)
        region=request.POST.get('region',)
        countrys = country(country_name=country_name,currency=currency,country_image=country_image,native_name=native_name,capital=capital,population=population,country_code=country_code,laguage=laguage,region=region,)
        countrys.save()
        return redirect('/country')
    return render(request,'country/add_country.html')

@login_required(login_url="/account/login/")
def update(request,id):
    countrys = country.objects.get(id=id)
    form = countryForm(request.POST or None, request.FILES, instance=countrys)
    if form.is_valid():
        form.save()
        return redirect('/country')
    return render(request,'country/edit.html',{'form':form,'country':countrys})

@login_required(login_url="/account/login/")
def delete(request,id):
    if request.method == "POST":
        countrys=country.objects.get(id=id)
        countrys.delete()
        return redirect('/country')
    return render(request,'country/delete.html')




class CountryListView(generics.ListCreateAPIView):
    queryset = country.objects.all()
    serializer_class = CountrySerializer
class CountryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = country.objects.all()
    serializer_class = CountrySerializer
@api_view(['GET','POST','PATCH','PUT','DELETE'])
def saveCountry(request):
    if request.method =="POST":
        saveSerialize = CountrySerializer(data=request.data)
        if saveSerialize.is_valid():
            saveSerialize.save()
            return Response(saveSerialize.data,status=status.HTTP_201_CREATED)
            return Response(saveSerialize.data,status=status.HTTP_400_BAD_REQUEST)
