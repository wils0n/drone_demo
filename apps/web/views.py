from django.shortcuts import render
from django.views.generic import TemplateView

class HomeTV(TemplateView):
	template_name="web/index.html"
