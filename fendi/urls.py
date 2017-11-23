from django.conf.urls import url
from .views import CrawlView

urlpatterns = [
    url(r'^$', CrawlView.as_view(), name='crawl'),
]
