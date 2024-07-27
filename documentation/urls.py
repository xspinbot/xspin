from django.urls import path
from documentation import views

urlpatterns = [
    path('', views.index, name='home'),
    path('games/', views.games, name='games'),
]