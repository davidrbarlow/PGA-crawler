
import scrapy
from scrapy.loader import ItemLoader
from pga_stats.items import expanded
import time
from scrapy_splash import SplashRequest
from scrapy.selector import Selector

class PGAStatsSpider(scrapy.Spider):
  #identiy
  name = 'expanded'
  custom_settings = {
          'ITEM_PIPELINES': {
              'pga_stats.pipelines.expanded': 500
          }
    }

  script = '''
function main(splash, args)
  assert(splash:go(args.url))
  treat=require('treat')
  result = {}
  assert(splash:wait(2))
 	result[1]=splash:html()
  assert(splash:wait(3))
  splash:set_viewport_full()
  return treat.as_array(result)
  end
  '''

  def start_requests(self):
   
    #start_urls = ['http://www.espn.com/golf/leaderboard/_/tournamentId/2512/season/2017']
    urls = ['http://www.espn.com/golf/statistics/_/year/{}/type/expanded/count/{}'.format(i,x) for i in range(2011, 2020) for x in [1,41,81,121,161]]
    print('urls',urls)
    #urls.append('http://www.espn.com/golf/statistics/_/type/expanded')
    #urls=['http://www.espn.com/golf/statistics/_/type/expanded']

    

#<!-- end Banner ad -->\

    for url in urls:
      print('-----------url',url)
      time.sleep(2)
      yield SplashRequest(url=url, callback=self.parse, endpoint='execute', args={'wait': 5, 'lua_source': self.script})

  #response
  def parse(self, response):
    
    for page in response.data:
      sel = Selector(text=page)
      
    #year = response.request.url.split('/')[8]
      year = sel.xpath("//h1[@class='h2']/text()").extract_first()
      if len(year.split('-')) == 3:
        year = '20'+str(year.split('-')[2]).strip()
      else:
        year = str(year.split('-')[1]).strip()
      
      print('year',year)
      print(type(year))
      time.sleep(4)
    #print('year', year)
      for player in sel.xpath("//tr[contains(@class,'oddrow') or contains(@class,'evenrow')]"):
        loader = ItemLoader(item=expanded(), selector=player, response=response)
        #print('----------tr',self.start_urls2)
        #print('----------pos',player.xpath("//child::td/text()").extract_first())
        #print('----------name',player.xpath("//child::td[2]/a/text()").extract_first())
        loader.add_xpath('rank',".//child::td/text()")
        loader.add_xpath('name',".//child::td[2]/a/text()") 
        loader.add_xpath('age',".//child::td[3]/text()")    
        loader.add_xpath('yardPerDrive',".//child::td[4]/text()")
        loader.add_xpath('driveAcc',".//child::td[5]/text()")
        loader.add_xpath('driveTotal',"..//child::td[6]/text()")
        loader.add_xpath('gir',".//child::td[7]/text()")
        loader.add_xpath('puttAvg',".//child::td[8]/text()")
        loader.add_xpath('savePCT',".//child::td[9]/text()")
        loader.add_value('year',year)

        yield loader.load_item()


   