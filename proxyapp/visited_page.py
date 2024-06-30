# views.py
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from requests.auth import HTTPProxyAuth
from .models import Proxy_information, VisitedPage

def scrape_website_with_proxy(url, user_ip, proxy_ip, proxy_port):
    # Proxy authentication
    proxy_auth = HTTPProxyAuth(proxy_ip, proxy_port)

    # Proxy settings for HTTP only
    proxies = {
        'http': f'http://{proxy_ip}:{proxy_port}',
    }

    # Make the request using the proxy
    response = requests.get(url, proxies=proxies, auth=proxy_auth)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extracting YouTube video URLs
    youtube_urls = []
    for iframe in soup.find_all('iframe'):
        src = iframe.get('src', '')
        if 'youtube.com/embed/' in src:
            video_id = src.split('/')[-1]
            youtube_urls.append(f'https://www.youtube.com/embed/{video_id}')

    # Extracting links
    links = []
    for a_tag in soup.find_all('a', href=True):
        link = urljoin(url, a_tag['href'])
        links.append(link)
        # Update the href attribute in the soup with the modified link
        a_tag['href'] = link

    # Prettify the HTML content
    content = soup.prettify()

    # Save visited page information in the database
    visited_page = VisitedPage.objects.create(
        ip_address=user_ip,
        proxy_ip=proxy_ip,
        proxy_port=proxy_port,
        visited_url=url,
        content=content
    )

    return content, youtube_urls, links, visited_page.id
# views.py
def display_visited_page(request, visited_page_id):
    visited_page = get_object_or_404(VisitedPage, pk=visited_page_id)

    # Pass the stored content to the template
    return render(request, 'testground/visited_page.html',
                  {'scraped_content': visited_page.content,
                   'youtube_urls': [],  # You can add logic to extract YouTube URLs if needed
                   'links': []})  # Similarly, extract links if needed

# model for it
class VisitedPage(models.Model):
    ip_address = models.GenericIPAddressField()
    proxy_ip = models.GenericIPAddressField()
    proxy_port = models.PositiveIntegerField()
    visited_url = models.URLField()
    content = models.TextField()

    def __str__(self):
        return f'{self.visited_url} - {self.ip_address}'