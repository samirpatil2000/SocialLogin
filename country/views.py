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
@login_required
def index(request):
    country_list = country.objects.all()
    context ={
        'country_list':country_list
    }
    return render(request,'country/index.html',context)

@login_required
def details(request,country_id): 
    try:
        countrys = country.objects.get(id=country_id)
    except country.DoesNotExist:
        countrys = None
    # countrys = country.objects.get(id=country_id)
    return render(request,'country/countryList.html',{'country':countrys})

@login_required
def add_country(request):
    if request.method == "POST":
        countryName=request.POST.get('countryName',)
        currency=request.POST.get('currency',)
        countryImage=request.FILES['countryImage']
        nativeName=request.POST.get('nativeName',)
        capital=request.POST.get('capital',)
        population=request.POST.get('population',)
        countryCode=request.POST.get('countryCode',)
        language=request.POST.get('language',)
        region=request.POST.get('region',)
        countrys = country(countryName=countryName,currency=currency,countryImage=countryImage,nativeName=nativeName,capital=capital,population=population,countryCode=countryCode,language=language,region=region,)
        countrys.save()
        return redirect('/country')
    return render(request,'country/addCountry.html')

@login_required
def update(request,id):
    try:
        countrys = country.objects.get(id=id)
    except country.DoesNotExist:
        countrys = None
    # countrys = country.objects.get(id=id)
    form = countryForm(request.POST or None, request.FILES, instance=countrys)
    if form.is_valid():
        form.save()
        return redirect('/country')
    return render(request,'country/editCountry.html',{'form':form,'country':countrys})

@login_required
def delete(request,id):
    if request.method == "POST":
        try:
            countrys=country.objects.get(id=id)
        except country.DoesNotExist:
            countrys = None
        # countrys=country.objects.get(id=id)
        countrys.delete()
        return redirect('/country')
    return render(request,'country/deleteCountry.html')

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