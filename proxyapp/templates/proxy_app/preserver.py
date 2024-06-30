
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from requests.auth import HTTPProxyAuth




















# second trier
def scrape_website_two(url):
    response = requests.get(url)
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

def fetch_dynamic_content(url):
    response = requests.get(url)
    return response.text

def display_content_two(request):
    # Replace 'https://example.com' with the URL of the website you want to scrape
    website_url = 'https://agrolearner.com/'

    # Scrape the content, video URLs, and links from the website
    scraped_content, youtube_urls, links = scrape_website_two(website_url)

    # Pass the scraped content, video URLs, and links to the template
    return render(request, 'testground/index2.html',
                  {'scraped_content': scraped_content, 'youtube_urls': youtube_urls, 'links': links})





# Proxy information
proxy_ip = '38.154.227.167'
proxy_port = 5868
proxy_username = 'testproxy1'
proxy_password = 'testproxy1'

# Proxy authentication
proxy_auth = HTTPProxyAuth(proxy_username, proxy_password)

# Function to scrape the website using the provided proxy
def scrape_website_with_proxy(url):
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

    return content, youtube_urls, links

# Function to fetch dynamic content using the provided proxy
def fetch_dynamic_content_with_proxy(url):
    # Proxy settings for HTTP only
    proxies = {
        'http': f'http://{proxy_ip}:{proxy_port}',
    }

    # Make the request using the proxy
    response = requests.get(url, proxies=proxies, auth=proxy_auth)
    return response.text

# Function to display content with the proxy
def display_content_with_proxy(request):
    # Replace 'https://example.com' with the URL of the website you want to scrape
    website_url = 'https://agrolearner.com/'

    # Scrape the content, video URLs, and links from the website using the proxy
    scraped_content, youtube_urls, links = scrape_website_with_proxy(website_url)

    # Pass the scraped content, video URLs, and links to the template
    return render(request, 'testground/index2.html',
                  {'scraped_content': scraped_content, 'youtube_urls': youtube_urls, 'links': links})