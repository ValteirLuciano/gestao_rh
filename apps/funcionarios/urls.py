from django.urls import path
from .views import FuncionariosListView, FuncionarioCreateView, FuncionarioUpdateView, FuncionarioDeleteView

urlpatterns = [
    path('', FuncionariosListView.as_view(), name='list_funcionarios'),
    path('novo/', FuncionarioCreateView.as_view(), name='create_funcionario'),
    path('editar/<int:pk>/', FuncionarioUpdateView.as_view(), name='update_funcionario'),
    path('delete/<int:pk>/', FuncionarioDeleteView.as_view(), name='delete_funcionario'),
]
