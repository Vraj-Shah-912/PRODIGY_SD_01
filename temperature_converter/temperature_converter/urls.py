# temperature_converter/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('converter.urls')),  # Include app's urls.py
]
