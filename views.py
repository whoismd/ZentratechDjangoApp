import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from .models import Product

def scrape(request, url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find('span', class_='_35KyD6').get_text()
    description = soup.find('div', class_='_3la3Fn').get_text()
    price = soup.find('div', class_='_30jeq3 _1_WHN1').get_text()
    mobile_number = soup.find('div', class_='_2aK_gu').get_text()
    size = soup.find('div', class_='_2xg6Ul').get_text()
    category = soup.find('div', class_='_2kHMtA').get_text()
    images = soup.find_all('img', class_='_2VeolH _3I5S6S')
    images = [img['src'] for img in images]

    product = Product(
        url=url,
        title=title,
        description=description,
        price=price,
        mobile_number=mobile_number,
        size=size,
        category=category,
        images=images
    )
    product.save()

    return render(request, 'scraper/scraped.html', {'product': product})
