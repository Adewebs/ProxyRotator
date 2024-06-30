# proxyapp/models.py
from django.db import models

class Proxy(models.Model):
    address = models.CharField(max_length=255)
    port = models.IntegerField()

    def __str__(self):
        return f"{self.address}:{self.port}"




class Proxy_information(models.Model):
    ip = models.GenericIPAddressField()
    port = models.PositiveIntegerField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.ip}:{self.port}'



class ScrapeURL(models.Model):
    url = models.URLField(unique=True)
    active_url = models.IntegerField(null=True,blank=True,default=0)

    def __str__(self):
        return f'{self.url}, {self.active_url}'


class VisitedPage(models.Model):
    ip_address = models.GenericIPAddressField()
    proxy_ip = models.GenericIPAddressField()
    proxy_port = models.PositiveIntegerField()
    visited_url = models.URLField()
    content = models.TextField()

    def __str__(self):
        return f'{self.visited_url}, {self.proxy_ip}'



class StreamingUrl(models.Model):
    stream_url = models.URLField(unique=True)
    stream_name = models.CharField(max_length=255,blank=True, null=True)

    def __str__(self):
        return f'{self.id}-{self.stream_name}- {self.stream_url}'