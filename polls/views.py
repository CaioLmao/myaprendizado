from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from .models import *

# Create your views here.

class IndexView (ListView):
    model = Membro
    template_name = "index.html"
    context_object_name = "membros"

class MembroView(DetailView):
    model = Membro
    template_name = "membro.html"

