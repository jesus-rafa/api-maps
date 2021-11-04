from django.contrib import admin
from django.urls import path

from . import views

app_name = "poligonos_app"

urlpatterns = [
    path('api/poligonos/', views.Lista_Poligonos.as_view()),
]
