from django.urls import path

from solos import views

app_name = 'solos'


urlpatterns = [
    path('recordings/<str:album>/<str:track>/<str:artist>/', views.solo_detail, name='solo_detail_view'),
    path('', views.index),
]
