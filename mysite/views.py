from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.



class HomeView(TemplateView):
    template_name = "main/index.html"


class AboutView(TemplateView):
    template_name = "main/about.html"

class ContactView(TemplateView):
    template_name = "main/contact.html"


