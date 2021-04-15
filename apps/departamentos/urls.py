from django.urls import path
from .views import DepartamentoListView, DepartamentoCreateView,DepartamentoUpdateView, DepartamentoDeleteView


urlpatterns = [
    path('list', DepartamentoListView.as_view(), name='list_departamentos'),
    path('novo', DepartamentoCreateView.as_view(), name='create-departamento'),
    path('editar/<int:pk>/', DepartamentoUpdateView.as_view(), name='update_departamento'),
    path('delete/<int:pk>/', DepartamentoDeleteView.as_view(), name='delete_departamento'),
]
