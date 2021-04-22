from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import RegistroHoraExtra
from django.urls import reverse_lazy
from .forms import RegistroHoraExtraForm


class RegistroHoraExtraListView(ListView):
    model = RegistroHoraExtra
    ordering = 'motivo'

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)


class RegistroHoraExtraCreateView(CreateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm
    success_url = reverse_lazy('list_hora_extra')

    def get_form_kwargs(self):
        kwargs = super(RegistroHoraExtraCreateView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class RegistroHoraExtraUpdateView(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm
    success_url = reverse_lazy('list_hora_extra')

    def get_form_kwargs(self):
        kwargs = super(RegistroHoraExtraUpdateView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class RegistroHoraExtraDeleteView(DeleteView):
    model = RegistroHoraExtra
    fields = ['motivo', 'funcionario', 'horas']
    success_url = reverse_lazy('list_hora_extra')
