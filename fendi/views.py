from django.shortcuts import redirect
from django.views.generic import FormView, ListView
from .forms import CrawlForm
from .models import Product
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


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
