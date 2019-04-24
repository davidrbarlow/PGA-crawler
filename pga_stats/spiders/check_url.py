import scrapy

class PGAStatsSpider(scrapy.Spider):
  #identiy
  name = 'check_url'


  #requests
  def start_requests(self):
    urls = [
      'http://www.espn.com/golf/statistics/_/type/expanded'
    ]

    for url in urls:
      yield scrapy.Request(url=url, callback=self.parse)

    


  #response
  def parse(self, response):
    page_number = '1'
    _file = "{0}.html".format(page_number)
    with open(_file, 'wb') as f:# wb intead of w
      f.write(response.body)