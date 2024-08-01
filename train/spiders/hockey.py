import scrapy
from scrapy.responsetypes import Response
from train.items import TeamItem

class HockeySpider(scrapy.Spider):
    name = "hockey"
    allowed_domains = ["www.scrapethissite.com"]
    start_urls = ["https://www.scrapethissite.com/pages/forms/"]

    def parse(self, response: Response):
        for i in range(1, 24):
            url: str = "https://www.scrapethissite.com/pages/forms/" + f"?page_num={i}" 
            yield response.follow(url, callback=self.parse_page)

    def parse_page(self, response: Response):
        teams = response.css("tr.team")
        team_item = TeamItem()

        for team in teams:
            team_item['name'] = team.css("td.name::text").get()
            team_item['year'] = team.css("td.year::text").get()
            team_item['wins'] = team.css("td.wins::text").get()
            team_item['losses'] = team.css("td.losses::text").get()
            team_item['ot_losses'] = team.css("td.ot-losses::text").get()
            team_item['win_percentage'] = team.css("td.pct::text").get()
            team_item['goals_for'] = team.css("td.gf::text").get()
            team_item['goals_against'] = team.css("td.ga::text").get()

            yield team_item

