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

from scrapy.selector import Selector

class PGAStatsSpider(scrapy.Spider):
  name = 'rbc_heritage_player2'

  script = '''
function main(splash, args)
  assert(splash:go(args.url))
  assert(splash:wait(1))
  treat=require('treat')
  result = {}
  assert(splash:runjs('document.querySelector(".leaderboard__content > div > div > a + a").click()'))
  assert(splash:wait(1))
  result[1]=splash:html()
  assert(splash:wait(2))
  splash:set_viewport_full()
  return treat.as_array(result)
  end
  '''

  def start_requests(self):
    #url = 'http://www.espn.com/golf/leaderboard/_/tournamentId/2242/season/2017'
    url = 'http://www.espn.com/golf/leaderboard/_/tournamentId/401025246/season/2017'
    #start_urls = ['http://www.espn.com/golf/leaderboard/_/tournamentId/401025246/season/{}'.format(i) for i in range(2001, 2019)]
    #yield SplashRequest(url=url, callback=self.parse, endpoint='render.html', args={'wait': 1})
    yield SplashRequest(url=url, callback=self.parse, endpoint='execute', args={'wait': 2, 'lua_source': self.script})
  
  def parse(self, response):
    print('-------res',type(response.data))
    for page in response.data:
      sel = Selector(text=page)
      #print('----------page',page)
      #print('----------sel',type(sel))
      for player in sel.xpath("(//tbody[@class='Table2__tbody'])[1]/child::tr"):
        #print('-----------row',sel.xpath("(//tbody[@class='Table2__tbody'])[1]/child::tr"))
        yield {
          'ip' : player.xpath(".//child::td[1]/text()").extract_first(),
          'name' : player.xpath(".//child::td[2]/a/text()").extract_first(),
          'driveYards' : player.xpath(".//child::td[3]/text()").extract_first(),
          'driveAcc' : player.xpath(".//child::td[4]/text()").extract_first(),
          'gir' : player.xpath(".//child::td[5]/text()").extract_first(),
          'ppgGir' : player.xpath(".//child::td[6]/text()").extract_first(),
          'eagle' : player.xpath(".//child::td[7]/text()").extract_first(),
          'birdie' : player.xpath(".//child::td[8]/text()").extract_first(),
          'pars' : player.xpath(".//child::td[9]/text()").extract_first(),
          'bogey' : player.xpath(".//child::td[10]/text()").extract_first(),
          'dbl' : player.xpath(".//child::td[11]/text()").extract_first(),
          'toPar' : player.xpath(".//child::td[12]/text()").extract_first(),
        }



