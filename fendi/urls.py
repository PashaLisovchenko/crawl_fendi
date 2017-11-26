from django.conf.urls import url
from .views import CrawlView, ProductListView

urlpatterns = [
    url(r'^$', CrawlView.as_view(), name='crawl'),
    url(r'^products/$', ProductListView.as_view(), name='products')
]
