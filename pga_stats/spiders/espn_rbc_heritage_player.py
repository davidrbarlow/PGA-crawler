#.leaderboard__content > div > div > a + a
# function main(splash, args)
#   assert(splash:go(args.url))
#   assert(splash:wait(0.5))
#   assert(splash:runjs('document.querySelector(".leaderboard__content > div > div > a + a").click()'))
#   assert(splash:wait(1))
#   splash:set_viewport_full()
#   return {
#     html = splash:html(),
#     png = splash:png(),
#     har = splash:har(),
#   }
# end

import scrapy
from scrapy_splash import SplashRequest
import time
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from pga_stats.items import rbcHeritagePlayer

class PGAStatsSpider(scrapy.Spider):
  name = 'rbc_heritage_player'
  custom_settings = {
        'ITEM_PIPELINES': {
            'pga_stats.pipelines.rbgHeritagePlayer': 500
        }
  }

  script = '''
function main(splash, args)
  assert(splash:go(args.url))
  treat=require('treat')
  result = {}
  assert(splash:runjs('document.querySelector(".leaderboard__content > div > div > a + a").click()'))
  assert(splash:wait(3))
  result[1]=splash:html()
  assert(splash:wait(3))
  splash:set_viewport_full()
  return treat.as_array(result)
  end
  '''

  def start_requests(self):
   
   #urls = ['http://www.espn.com/golf/leaderboard/_/tournamentId/2242/season/{}'.format(i) for i in range(2012, 2014)]
    urls = [
    'http://www.espn.com/golf/leaderboard/_/tournamentId/401025246',
    'http://www.espn.com/golf/leaderboard/_/tournamentId/2701',
    'http://www.espn.com/golf/leaderboard/_/tournamentId/2494',
    'http://www.espn.com/golf/leaderboard/_/tournamentId/2242',
    'http://www.espn.com/golf/leaderboard/_/tournamentId/1318',
    'http://www.espn.com/golf/leaderboard/_/tournamentId/1193',
    'http://www.espn.com/golf/leaderboard/_/tournamentId/1006',
    'http://www.espn.com/golf/leaderboard/_/tournamentId/903',
  ]

    # urls = [
    # 'http://www.espn.com/golf/leaderboard/_/tournamentId/1193',
    # ]


    for url in urls: 
      print('-----------url',url)
      print('-----------yielding',url)
      yield SplashRequest(url=url, callback=self.parse, endpoint='execute', args={'wait': 5, 'lua_source': self.script})
    
#//span[@class='Leaderboard__Event__Date']

  def parse(self, response):
    print('-------parse')
    if response.data != None:
      #print('--------------requ url ',response.request.url )
      #print('--------------requ url ',response.request.url.split('/')[7])

      for page in response.data:
        sel = Selector(text=page)
        date = sel.xpath("//span[@class='Leaderboard__Event__Date n7']/text()").extract_first()
        year = str(date.split(',')[1]).strip()
        print('---------- year',year)
        #print('----------sel',type(sel))
        for player in sel.xpath("(//tbody[@class='Table2__tbody'])[1]/child::tr"):
          #print('-----------row',sel.xpath("(//tbody[@class='Table2__tbody'])[1]/child::tr"))
          loader = ItemLoader(item=rbcHeritagePlayer(), selector=player, response=response)
          loader.add_xpath('ip',".//child::td[1]/text()")
          loader.add_xpath('name',".//child::td[2]/a/text()")
          loader.add_xpath('driveYards',".//child::td[3]/text()")
          loader.add_xpath('driveAcc',".//child::td[4]/text()")
          loader.add_xpath('gir',".//child::td[5]/text()")
          loader.add_xpath('ppgGir',".//child::td[6]/text()")
          loader.add_xpath('eagle',".//child::td[7]/text()")
          loader.add_xpath('birdie',".//child::td[8]/text()")
          loader.add_xpath('pars',".//child::td[9]/text()")
          loader.add_xpath('bogey',".//child::td[10]/text()")
          loader.add_xpath('dbl',".//child::td[11]/text()")
          loader.add_xpath('toPar',".//child::td[12]/text()")
          loader.add_value('year',year)
          yield loader.load_item()
        



