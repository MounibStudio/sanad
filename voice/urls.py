from django.urls import path
from . import views

app_name = 'voice'

urlpatterns = [
    path('', views.ask, name='index'),  # 'index' keeps core:home link working
    path('ask/', views.ask, name='ask'),
]
