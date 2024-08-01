import scrapy
from train.items import OscarItem


class OscarSpider(scrapy.Spider):
    name = "oscar"
    allowed_domains = ["www.scrapethissite.com"]
    start_urls = ["https://www.scrapethissite.com/pages/ajax-javascript/"]


    def parse(self, response):
        for i in range(6):
            url = self.start_urls[0] + f"?ajax=true&year=201{i}"
            yield response.follow(url, callback=self.parse_item)


    def parse_item(self, response):
        item = OscarItem()
        movies = response.json()

        for movie in movies:
            item['title'] = movie['title']
            item['year'] = movie['year']
            item['awards'] = movie['awards']
            item['nominations'] = movie['nominations']
            try:
                item['best_picture'] = movie['best_picture']
            except:
                pass

            yield item

