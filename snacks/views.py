from django.db.models import fields
from django.shortcuts import render

from django.views.generic import (ListView,DetailView,CreateView,DeleteView,UpdateView)
from snacks.models import Snack
from django.urls import reverse_lazy

class SnackListView(ListView):
    template_name = 'list-snacks.html'
    model = Snack
    

class SnackDetailView(DetailView):
    template_name = 'details-snack.html'
    model = Snack
    context_object_name = 'detailsSnack'


class SnackCreateView(CreateView):
    template_name = 'create-snack.html'
    model = Snack
    fields = ['title','description' ,'purchaser']

class SnackUpdateView(UpdateView):
    template_name = 'update-snack.html'
    model = Snack
    fields = ['title','description' , 'purchaser']

class SnackDeleteView(DeleteView):
    template_name = 'delete-snack.html'
    model = Snack
    success_url = reverse_lazy('all')
