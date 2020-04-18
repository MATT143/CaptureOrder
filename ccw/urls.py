from django.urls import path
from .views import home,orderData


urlpatterns = [
    path('',home,name="home" ),
    path('data',orderData,name="data" ),
]
