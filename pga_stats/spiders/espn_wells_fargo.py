
import scrapy
from scrapy.loader import ItemLoader
from pga_stats.items import rbcHeritage
import time

class PGAStatsSpider(scrapy.Spider):
  #identiy
  name = 'wells_fargo'
  custom_settings = {
          'ITEM_PIPELINES': {
              'pga_stats.pipelines.wellsFargo': 400
          }
    }

  def start_requests(self):
   
    #start_urls = ['http://www.espn.com/golf/leaderboard/_/tournamentId/2512/season/2017']
    #start_urls = ['http://www.espn.com/golf/leaderboard/_/tournamentId/2242/season/{}'.format(i) for i in range(2001, 2019)]
    # urls = ['http://www.espn.com/golf/leaderboard/_/tournamentId/401056528',
    # 'http://www.espn.com/golf/leaderboard/_/tournamentId/401025246']
    urls = [
      'http://www.espn.com/golf/leaderboard/_/tournamentId/401025249',
      'http://www.espn.com/golf/leaderboard/_/tournamentId/3067',
      'http://www.espn.com/golf/leaderboard/_/tournamentId/2520',
      'http://www.espn.com/golf/leaderboard/_/tournamentId/2268',
      'http://www.espn.com/golf/leaderboard/_/tournamentId/1342',
      'http://www.espn.com/golf/leaderboard/_/tournamentId/1216',
      'http://www.espn.com/golf/leaderboard/_/tournamentId/1028',
      'http://www.espn.com/golf/leaderboard/_/tournamentId/921'
    ]

    for url in urls:
      yield scrapy.Request(url=url, callback=self.parse)

  #response
  def parse(self, response):
    
    #year = response.request.url.split('/')[9]
    time.sleep(2)
    try:
      response.xpath
      print('test')
    except:
      print('Lookup failed.  Trying again...')
      time.sleep(2)
      yield scrapy.Request(url=response.url, callback=self.parse, dont_filter=True)
    else:
      print('else')
      
      date = response.xpath("//span[@class='Leaderboard__Event__Date n7']/text()").extract_first()
      year = str(date.split(',')[1]).strip()
      if (year in ['2016','2013','2012','2011']):
        table_number = '2'
      else:
        table_number = '1'
      for player in response.xpath("(//tbody[@class='Table2__tbody'])[{}]/child::tr".format(table_number)):
        loader = ItemLoader(item=rbcHeritage(), selector=player, response=response)
        #print('----------tr',self.start_urls2)
        print('----------pos',player.xpath("//child::td/text()").extract_first())
        print('----------name',player.xpath("//child::td[2]/a/text()").extract_first())
        loader.add_xpath('rank',".//child::td/text()")
        loader.add_xpath('name',".//child::td[2]/a/text()")    
        loader.add_xpath('score',".//child::td[3]/text()")
        loader.add_xpath('r1',".//child::td[4]/text()")
        loader.add_xpath('r2',".//child::td[5]/text()")
        loader.add_xpath('r3',".//child::td[6]/text()")
        loader.add_xpath('r4',".//child::td[7]/text()")
        loader.add_xpath('total',".//child::td[8]/text()")
        loader.add_xpath('earnings',".//child::td[9]/text()")
        loader.add_xpath('fedExPoints',".//child::td[10]/text()")
        loader.add_value('year',year)

        yield loader.load_item()


   