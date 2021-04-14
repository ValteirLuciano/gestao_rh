from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from .models import Empresa

from django.urls import reverse_lazy


class EmpresaCreateView(CreateView):
    model = Empresa
    fields = ['nome',]
    #success_url = reverse_lazy('home')

    def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = obj
        funcionario.save()
        return HttpResponse('Ok')


class EmpresaUpdateView(UpdateView):
    model = Empresa
    fields = ['nome', ]
    success_url = reverse_lazy('home')
