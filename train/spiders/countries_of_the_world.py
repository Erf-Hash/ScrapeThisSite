import scrapy
from scrapy.responsetypes import Response
from train.items import CountryItem

class CountriesOfTheWorldSpider(scrapy.Spider):
    name = "countries_of_the_world"
    allowed_domains = ["www.scrapethissite.com"]
    start_urls = ["https://www.scrapethissite.com/pages/simple/"]

    def parse(self, response: Response):
        country = CountryItem()
        name: list = response.css("h3.country-name::text").getall()
        capital: list = response.css("span.country-capital::text").getall()
        population: list = response.css("span.country-population::text").getall()
        area: list = response.css("span.country-area::text").getall()

        for i in range(len(capital)):
            country['name'] = name[(2 * i) + 1]
            country['capital'] = capital[i]
            country['population'] = population[i]
            country['area'] = area[i]

            yield country 

