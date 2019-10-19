from scrapy import cmdline

cmdline.execute("scrapy crawl lotterySpider -s LOG_ENABLED=False".split())
