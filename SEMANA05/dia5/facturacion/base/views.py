from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

class Index(LoginRequiredMixin,generic.TemplateView):
    template_name = 'index.html'
    login_url='/login/'