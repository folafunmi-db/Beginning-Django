from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

# Note that class names are Pascal cased
class HomePageView(TemplateView):
  template_name = 'home.html'