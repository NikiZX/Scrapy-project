import scrapy
from ..items import productInfo
import json


class MangoSpider(scrapy.Spider):
    name = 'MangoSpider'
    start_urls = ['https://shop.mango.com/services/garments/006/en/S/17042020','https://shop.mango.com/services/garments/006/en/S/47095923']

    def parse(self, response):
        jsonresponse = json.loads(response.text)
        product_info = productInfo()
        product_info["name"] = jsonresponse.get("name", "")
        product_info["price"] = str(jsonresponse.get("price", "").get("price", "")) + " " +jsonresponse.get("price", "").get("currency", "")
        color_and_sizes = self.get_color_and_sizes(response)
        product_info["color"] = color_and_sizes[0]
        product_info["size"] = color_and_sizes[1]
        yield(product_info)

    def get_color_and_sizes(self, response):
        color_and_sizes = []
        size_availability = []
        jsonresponse = json.loads(response.text)
        selected_info = jsonresponse.get("colors", "").get("colors", "")

        for i in selected_info:
            if(i.get("default", "") == True):
                color_and_sizes.append(i.get("label", ""))
                sizes = i.get("sizes", "")

        for item in sizes:
            available = item.get("available", "False")
            size=item.get("value")
            size_availability.append({size:available})

        color_and_sizes.append(size_availability)

        return color_and_sizes