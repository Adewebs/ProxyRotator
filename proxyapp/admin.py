from django.contrib import admin
from .models import Proxy, Proxy_information, ScrapeURL, VisitedPage, StreamingUrl

# Register your models here.
admin.site.register(Proxy)
admin.site.register(Proxy_information)
admin.site.register(StreamingUrl)
admin.site.register(ScrapeURL)
admin.site.register(VisitedPage)