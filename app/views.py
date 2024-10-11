from django.shortcuts import render
from django.views.generic import TemplateView

class HomepageView(TemplateView):
    template_name = 'app/Home.html'

class AboutpageView(TemplateView):
    template_name = 'app/About.html'

