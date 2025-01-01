from dis import Positions

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Client, Order, Photo, PrintOption, Payment


class HomepageView(TemplateView):
    template_name = 'app/Home.html'

class AboutpageView(TemplateView):
    template_name = 'app/About.html'
    
    
class ClientListView(ListView):
    model = Client
    context_object_name = 'client'
    template_name = 'app/client_list.html'
    context_object_name = 'client'

class ClientDetailView(DetailView):
    model = Client
    context_object_name = 'client'
    template_name = 'app/client_detail.html'

class ClientCreateView(CreateView):
    model = Client
    fields = ['name', 'email', 'contact_number', 'address']
    template_name = 'app/client_create.html'
    success_url = '/client/'

class ClientUpdateView(UpdateView):
    model = Client
    fields = ['name', 'email', 'contact_number', 'address']
    template_name = 'app/client_update.html'
    success_url = '/client/'

class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'app/client_delete.html'
    success_url = reverse_lazy('client_list')




