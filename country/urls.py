from django.conf.urls import url,include
from django.contrib import admin
from django.urls import path
from country import views


app_name = 'country'
urlpatterns = [
    path('',views.index,name='index'),
    path('country/<int:country_id>/',views.details,name='details'),
    path('add/',views.add_country,name='add_country'),
    path('edit/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),

    path('country-rest/',views.CountryListView.as_view(),name="list_country"),
    path('country-rest/<int:pk>',views.CountryDetailView.as_view(),name="detail_country"),
    
]