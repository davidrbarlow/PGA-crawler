
import scrapy
from scrapy.loader import ItemLoader
from pga_stats.items import sgOffTheTee

class PGAStatsSpider(scrapy.Spider):
  #identiy
  name = 'sg_off_the_tee'
  custom_settings = {
          'ITEM_PIPELINES': {
              'pga_stats.pipelines.sgOffTheTee': 600
          }
    }
  start_urls = [
      'https://www.pgatour.com/stats/stat.02567.2019.html'
    ]

  #response
  def parse(self, response):

    year = response.request.url.split('.')[4]

    #for quote in response.selector.xpath("//div[@class='quote']"):
    # for quote in response.xpath("//div[@class='quote']"):
    #   loader = ItemLoader(item=QuoteItem(), selector=quote, response=response)
    #   loader.add_xpath('text',".//div[@class='quoteText']/text()[1]")
    #   loader.add_xpath('author',".//div[@class='quoteText']/child::span[@class='authorOrTitle']/text()")
    #   loader.add_xpath('tags',".//div[@class='greyText smallText left']/a/text()")
    #   yield loader.load_item()

    # yield {
    #   'text': quote.xpath(".//div[@class='quoteText']/text()[1]").extract_first(),
    #   'author': quote.xpath(".//div[@class='quoteText']/child::span[@class='authorOrTitle']/text()").extract_first(),
    #   'tags': quote.xpath(".//div[@class='greyText smallText left']/a/text()").extract(),
    # }

    for player in response.xpath("//table[@class='table-styled']/child::tbody/child::tr"):
      loader = ItemLoader(item=pgaStatsItem(), selector=player, response=response)
      loader.add_xpath('week_rank',".//child::td[1]/text()")
      loader.add_xpath('rank_last_week',".//child::td[2]/text()")
      loader.add_xpath('name',".//td[@class='player-name']/a/text()[1]")
      loader.add_xpath('rounds',".//child::td[4]/text()")
      loader.add_xpath('average',".//child::td[5]/text()")
      loader.add_xpath('total',".//child::td[6]/text()")
      loader.add_xpath('measured_rounds',".//child::td[7]/text()")
      loader.add_value('year',year)

      yield loader.load_item()

      # print("--------------")
      # print('week_rank',player.xpath(".//child::td[1]/text()").extract_first())
      # print('rank_last_week',player.xpath(".//child::td[2]/text()").extract_first())
      # #print('rank_last_week',player.xpath(".//child::td/following-sibling::td/text()").extract_first())
      # print('name',player.xpath(".//td[@class='player-name']/a/text()[1]").extract_first())
      # print('rounds',player.xpath(".//child::td[4]/text()").extract_first())
      # print('average',player.xpath(".//child::td[5]/text()").extract_first())
      # print('total',player.xpath(".//child::td[6]/text()").extract_first())
      # print('measured',player.xpath(".//child::td[7]/text()").extract_first())
      # yield {
      #   'week_rank':player.xpath(".//child::td[1]/text()").extract_first(),
      #   'rank_last_week':player.xpath(".//child::td[2]/text()").extract_first(),
      #   'player_name': player.xpath(".//td[@class='player-name']/a/text()[1]").extract_first(),
      #   'rounds': player.xpath(".//child::td[4]/text()").extract_first(),
      #   'average': player.xpath(".//child::td[5]/text()").extract_first(),
      #   'total': player.xpath(".//child::td[6]/text()").extract_first(),
      #   'measured_rounds': player.xpath(".//child::td[7]/text()").extract_first(),
      # }


   