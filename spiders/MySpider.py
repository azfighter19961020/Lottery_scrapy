import scrapy
from lottery.items import LotteryItem

class MySpider(scrapy.Spider):
    name = 'lotterySpider'
    start_urls=['https://www.taiwanlottery.com.tw/lotto/lotto649/history.aspx']

    def parse(self,response):
        data = response.body.decode()
        #with open('html.txt','w+') as f:
        #    f.write(data)
        selector = scrapy.Selector(text=data)
        total = selector.xpath('//*[@id="Lotto649Control_history_dlQuery"]/tr/td/table')
        for lottery in total:
            item = LotteryItem()
            item['turn'] = lottery.xpath('./tr[2]/td[1]/span/text()').extract()[0]
            item['dateOpen'] = lottery.xpath('./tr[2]/td[2]/span/span/text()').extract()[0]
            item['dateClose'] = lottery.xpath('./tr[2]/td[3]/span/text()').extract()[0]
            item['totalPrize'] = lottery.xpath('./tr[2]/td[5]/span/text()').extract()[0]
            totalNumber  = lottery.xpath('./tr[4]')
            totalNumberSelector = scrapy.Selector(text = totalNumber.extract()[0])
            totalNumberPath = totalNumberSelector.xpath('//td')
            item['lotteryNumber'] = totalNumberPath.xpath('./span/text()').extract()
            item['lotteryNumberSpecial'] = totalNumberPath.xpath('./span/span/text()').extract()[0]
            yield item
