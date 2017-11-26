from django.shortcuts import render, redirect
from django.views.generic import FormView
from .forms import CrawlForm
import redis


class CrawlView(FormView):
    template_name = 'index.html'
    form_class = CrawlForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        cd = form.cleaned_data
        name_spider = cd['name_spider']
        url_category = cd['url_category']
        r = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
        r.lpush(name_spider+':start_urls', url_category)
        return redirect('/')
