from django.urls import path
from . import views

urlpatterns = [

# path('checkingtwo', views.display_content_two, name='checkingtwo'),
    path('', views.home_page, name ="homepage"),
path('checkingthree', views.display_content_with_proxy, name='checkingthree'),
    path('streaming/<int:pk>/', views.streaming_link, name='streaming'),
path('streamingtwo', views.streaming_link_two, name='streamingtwo')



]