from django.urls import path
from . import views

app_name = 'voice'

urlpatterns = [
    # Dev A: add voice recording and playback routes here
    path('', views.index, name='index'),
]
