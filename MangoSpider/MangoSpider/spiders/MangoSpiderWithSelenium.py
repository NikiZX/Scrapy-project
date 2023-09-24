import scrapy
from ..items import productInfo
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class MangoSpiderWithSelenium(scrapy.Spider):

    name = 'MangoSpiderWithSelenium'
    start_urls = ['https://shop.mango.com/bg-en/men/t-shirts-plain/100-linen-slim-fit-t-shirt_47095923.html?c=07','https://shop.mango.com/gb/women/skirts-midi/midi-satin-skirt_17042020.html?c=99']

    def start_requests(self):
        yield from [SeleniumRequest(url=url, callback=self.parse, wait_time=5,wait_until=EC.presence_of_element_located((By.CSS_SELECTOR, '[itemprop="priceCurrency"]'))) for url in self.start_urls]

    def parse(self, response, **kwargs):
        product_info = productInfo()
        product_info['name'] = response.css('h1.product-name::text').get()
        product_info['color'] = response.css('span.colors-info-name::text').get()
        product_info['price'] = str(response.css('[itemprop="price"] ::attr(content)').get()) + ' ' + response.css('[itemprop="priceCurrency"]::attr(content)').get()
        product_info['size'] = self.get_size(response)
        return(product_info)

    def get_size(self, response):
        sizes = []
        base_locator = 'button[data-testid*="pdp.sizeSelector.size"]'

        for raw_size in response.css(base_locator):
            is_available = not bool(raw_size.css('[data-testid*="unavailable"]'))
            size = raw_size.css("[id*=size]::text").get()
            sizes.append({size: is_available})

        return sizes