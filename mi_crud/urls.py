
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('lista_productos', permanent=False)), 
    path('admin/', admin.site.urls),
    path('productos/', include('productos.urls')),

]
