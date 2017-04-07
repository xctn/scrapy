from scrapy.spider import Spider  
from scrapy.selector import Selector

from tutorial.items import DmozItem 
  
class DmozSpider(Spider):  
    name = "dmoz"  
    allowed_domains = ["today.hitwh.edu.cn"]  
    start_urls = [ 
     "http://today.hitwh.edu.cn/news_more_list.asp?id=7"  
    ]  
  
    def parse(self, response):  
        sel = Selector(response)  
        sites = sel.xpath('//div[@id="righ_list"]/ul/li')  
        items = []  
        for site in sites:  
            item = DmozItem()  
            item['title'] = site.xpath('a/text()').extract()  
            item['link'] = site.xpath('a/@href').extract()  
            item['desc'] = site.xpath('text()').extract()  
            items.append(item)  
        return items 
