from django.shortcuts import render
from django.views.generic import FormView
from .forms import CrawlForm


class CrawlView(FormView):
    template_name = 'index.html'
    form_class = CrawlForm
    success_url = '/'
