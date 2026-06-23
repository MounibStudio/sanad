from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('voice/', include('voice.urls', namespace='voice')),
    path('accessibility/', include('accessibility.urls', namespace='accessibility')),
    # Dev B branches will wire these:
    path('knowledge/', include('knowledge.urls', namespace='knowledge')),
]
