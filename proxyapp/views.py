from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from requests.auth import HTTPProxyAuth
import random
import re
import logging

logger = logging.getLogger(__name__)
from .models import Proxy_information, ScrapeURL, VisitedPage, StreamingUrl


def streaming_link_two(request):
    # Set the proxy details
    PROXY_IP = '38.154.227.167'
    PROXY_PORT = '5868'
    PROXY_USERNAME = 'testproxy1'
    PROXY_PASSWORD = 'testproxy1'

    # Construct the proxy URL with username and password
    PROXY_URL = f'http://{PROXY_USERNAME}:{PROXY_PASSWORD}@{PROXY_IP}:{PROXY_PORT}'

    # Set up the proxy for the request
    proxies = {
        'http': PROXY_URL,
        'https': PROXY_URL,
    }

    # Make a request using the configured proxy
    response = requests.get('https://streamfinder.com/', proxies=proxies, verify=False)

    # Get the HTML content from the response
    html_content = response.text

    # Pass the HTML content to the template
    return render(request, 'testground/streaming2.html', {'html_content': html_content})

#stream
def streaming_link(request, pk):
    get_stream_url = StreamingUrl.objects.get(id=pk)
    stream_url = get_stream_url.stream_url

    return render(request, 'testground/streaming.html', {"stream_link": stream_url})
# def embed_link(request):
#     # Check if the 'embed_link' parameter is present in the request's GET parameters
#     if 'embed_link' in request.GET:
#         # Get the original URL from the request
#         iframe_url = request.GET['embed_link']
#
#         # Define the proxy URL and port
#         proxy_url = 'http://38.154.227.167:5868/'
#
#         # Modify the original URL to use the proxy
#         modified_url = re.sub(r'^https?://', proxy_url, iframe_url)
#
#         # Pass the modified URL to the template context
#         context = {'embed_link': modified_url}
#     else:
#         # If 'embed_link' parameter is not present, provide an empty context
#         context = {}
#
#     # Render the template with the context
#     return render(request, 'testground/streaming.html', context)

#home
def home_page(request):
    return render(request, "testground/index.html")

# Function to scrape the website using the selected proxy
def scrape_website_with_proxy(url):
    # Fetch a random proxy from the database
    random_proxy = Proxy_information.objects.order_by('?').first()

    # Proxy authentication
    proxy_auth = HTTPProxyAuth(random_proxy.username, random_proxy.password)

    # Proxy settings for HTTP only
    proxies = {
        'http': f'http://{random_proxy.ip}:{random_proxy.port}',
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

    return content, youtube_urls, links

# Function to fetch dynamic content using the selected proxy
def fetch_dynamic_content_with_proxy(url):
    # Fetch a random proxy from the database
    random_proxy = Proxy_information.objects.order_by('?').first()

    # Proxy authentication
    proxy_auth = HTTPProxyAuth(random_proxy.username, random_proxy.password)

    # Proxy settings for HTTP only
    proxies = {
        'http': f'http://{random_proxy.ip}:{random_proxy.port}',
    }

    # Make the request using the proxy
    response = requests.get(url, proxies=proxies, auth=proxy_auth)
    return response.text

# Function to display content with the selected proxy
def display_content_with_proxy(request):
    webs_link = ScrapeURL.objects.get(active_url = 1)
    new_url = webs_link.url

    # Replace 'https://example.com' with the URL of the website you want to scrape
    website_url = f'{new_url}'

    # Scrape the content, video URLs, and links from the website using the selected proxy
    scraped_content, youtube_urls, links = scrape_website_with_proxy(website_url)

    # Pass the scraped content, video URLs, and links to the template
    return render(request, 'testground/index2.html',
                  {'scraped_content': scraped_content, 'youtube_urls': youtube_urls, 'links': links})


#this is for dyanmically stating the url
# Function to scrape the website using the selected proxy
# def scrape_website_with_proxy(request):
#     # Fetch a random proxy from the database
#     random_proxy = ProxyInformation.objects.order_by('?').first()
#
#     # Fetch the target website URL from the database
#     scrape_url = ScrapeURL.objects.order_by('?').first()
#
#     # Proxy authentication
#     proxy_auth = HTTPProxyAuth(random_proxy.username, random_proxy.password)
#
#     # Proxy settings for HTTP only
#     proxies = {
#         'http': f'http://{random_proxy.ip}:{random_proxy.port}',
#     }
#
#     # Make the request using the proxy
#     response = requests.get(scrape_url.url, proxies=proxies, auth=proxy_auth)
#     soup = BeautifulSoup(response.text, 'html.parser')
#
#     # Extracting YouTube video URLs
#     youtube_urls = []
#     for iframe in soup.find_all('iframe'):
#         src = iframe.get('src', '')
#         if 'youtube.com/embed/' in src:
#             video_id = src.split('/')[-1]
#             youtube_urls.append(f'https://www.youtube.com/embed/{video_id}')
#
#     # Extracting links
#     links = []
#     for a_tag in soup.find_all('a', href=True):
#         link = urljoin(scrape_url.url, a_tag['href'])
#         links.append(link)
#         # Update the href attribute in the soup with the modified link
#         a_tag['href'] = link
#
#     # Prettify the HTML content
#     content = soup.prettify()
#
#     return content, youtube_urls, links
#
# # Function to display content with the selected proxy
# def display_content_with_proxy(request):
#     # Scrape the content, video URLs, and links from the website using the selected proxy
#     scraped_content, youtube_urls, links = scrape_website_with_proxy(request)
#
#     # Pass the scraped content, video URLs, and links to the template
#     return render(request, 'testground/index2.html',
#                   {'scraped_content': scraped_content, 'youtube_urls': youtube_urls, 'links': links})