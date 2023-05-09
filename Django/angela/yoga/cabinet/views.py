from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView

from basket.models import Basket
from cabinet.forms import CabinetForm
from users.models import User


class CabinetView(UpdateView):
    model = User
    form_class = CabinetForm
    template_name = 'cabinet/cabinet.html'

    def get_success_url(self):
        return reverse_lazy('cabinet', args=(self.object.id,))


