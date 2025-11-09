# # from django.contrib import admin
# from django.urls import path
# from .views import index,Home

# urlpatterns = [
#    path('in/', index,name="index"),
#    path('home/', Home ,name="Home"),
# ]
from django.urls import path 
from . import views

urlpatterns=[
    path('',views.contact),
    # path('contact/',views.contact,name="savecontact")
]