from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    # Dev A branches will wire these:
    path('voice/', include('voice.urls', namespace='voice')),
    # Dev B branches will wire these:
    path('knowledge/', include('knowledge.urls', namespace='knowledge')),
]
