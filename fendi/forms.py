from django import forms

SPIDER_CHOICES = [('fendi', 'fendi')]
URL_CHOICES = [('https://fendi.com/us/man', 'https://fendi.com/us/man'),
               ('https://fendi.com/us/woman', 'https://fendi.com/us/woman')
               ]


class CrawlForm(forms.Form):
    name_spider = forms.TypedChoiceField(choices=SPIDER_CHOICES)
    url_category = forms.TypedChoiceField(choices=URL_CHOICES)
