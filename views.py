import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from .models import ScrapedProduct
from datetime import datetime, timedelta

class ScraperView(View):
    def get(self, request, url):
        product = ScrapedProduct.objects.filter(url=url).first()
        if product and (datetime.now() - product.scraped_at).days < 7:
            return render(request, 'scraper/scraped.html', {'product': product})
        else:
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            title = soup.find('span', class_='product-title').get_text()
            description = soup.find('div', class_='product-description').get_text()
            price = soup.find('div', class_='product-price').get_text()
            mobile_number = soup.find('div', class_='product-mobile-number').get_text()
            size = soup.find('div', class_='product-size').get_text()
            category = soup.find('div', class_='product-category').get_text()
            images = soup.find_all('img', class_='product-image')
            images = [img['src'] for img in images]
            if product:
                product.title = title
                product.description = description
                product.price = price
                product.mobile_number = mobile_number
                product.size = size
                product.category = category
                product.images = images
                product.scraped_at = datetime.now()
                product.save()
            else:
                product = ScrapedProduct(
                    url=url,
                    title=title,
                    description=description,
                    price=price,
                    mobile_number=mobile_number,
                    size=size,
                    category=category,
                    images=images,
                    scraped_at=datetime.now()
                )
                product.save()
            return render(request, 'scraper/scraped.html', {'product': product})

