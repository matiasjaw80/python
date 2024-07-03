from django.contrib import admin
from django.urls import path, include
from AppColegio import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('app-colegio/', include('AppColegio.urls')),
    path('', views.index)
]
