from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import User
from .forms import RegistrationForm
from django.http import JsonResponse
from django.contrib.messages.views import SuccessMessageMixin
import json

class CreateUsers(SuccessMessageMixin, CreateView):
    model = User
    form_class = RegistrationForm
    success_url = '/usuarios/cadastrar/'
    template_name = 'user/user_create.html'
    success_message = 'Cadastrado com Sucesso!'


class ListUsers(ListView):
    model = User
    queryset: User.objects.all()
    template_name = 'user/user_list.html'

def json(request):
    data = list(User.objects.values())
    return JsonResponse(data, safe=False)