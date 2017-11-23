from django import forms


class CrawlForm(forms.Form):
    name_spider = forms.CharField()
    url_category = forms.CharField()
