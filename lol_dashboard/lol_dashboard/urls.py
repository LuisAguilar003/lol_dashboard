from django.contrib import admin
from django.urls import path
from campeones import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.lista_campeones, name='lista_campeones'),
]
