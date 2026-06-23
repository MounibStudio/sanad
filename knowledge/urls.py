from django.urls import path
from . import views

app_name = 'knowledge'

urlpatterns = [
    # Dev B: add FAQ search and answer routes here
    path('', views.index, name='index'),
]
