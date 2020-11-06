from django.urls import path
from . import views
urlpatterns = [
    path('', views.hi, name='HOME'),
    path('home', views.homee, name='HOME'),
    path('about', views.about, name='About'),
    path('service', views.service, name='Services')
]