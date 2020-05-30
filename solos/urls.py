from django.urls import path

from solos import views

app_name = 'solos'


urlpatterns = [
    path('solos/<int:pk>/', views.SoloDetailView.as_view()),
    path('', views.index),
]
