
from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", views.Sum),
    path('cal/', views.Calculate),
    path('mul/', views.Mul),
    path('asd/', views.asd),
    
    
]
