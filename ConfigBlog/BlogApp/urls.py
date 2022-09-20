from django.urls import path
from .views import  Inicio, ArticuloDetailView, Crearpost, Crearcategoria, Actualizar, BorrarPost




urlpatterns = [
    path('', Inicio.as_view(), name='inicio'),
    path('articulo/<int:pk>/', ArticuloDetailView.as_view(), name='articulo'),
    path('agregar/', Crearpost.as_view(), name='agregar'),
    path('categoria/', Crearcategoria.as_view(), name='categoria'),
    path('actualizar/<int:pk>/', Actualizar.as_view(), name='actualizar'),
    path('eliminar/<int:pk>/', BorrarPost.as_view(), name='eliminar'),
]