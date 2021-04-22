from django.urls import path
from .views import (
    RegistroHoraExtraListView,
    RegistroHoraExtraCreateView,
    RegistroHoraExtraUpdateView,
    RegistroHoraExtraDeleteView
)


urlpatterns = [
    path('', RegistroHoraExtraListView.as_view(), name='list_hora_extra'),
    path('novo/', RegistroHoraExtraCreateView.as_view(), name='create_hora_extra'),
    path('editar/<int:pk>/', RegistroHoraExtraUpdateView.as_view(), name='update_hora_extra'),
    path('delete/<int:pk>/', RegistroHoraExtraDeleteView.as_view(), name='delete_hora_extra'),
]