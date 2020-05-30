from django.urls import path

from solos import views

app_name = 'solos'


urlpatterns = [
    path('', views.index),
]
