# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class LotteryPipeline(object):
    count = 0
    def process_item(self, item, spider):
        fobj = open('output.csv','a+')
        writer = csv.writer(fobj)
        if LotteryPipeline.count == 0:
            writer.writerow(['期別','開獎日','兌獎截止','獎金總額','獎號','特別號'])
            writer.writerow([item['turn'],item['dateOpen'],item['dateClose'],item['totalPrize'],item['lotteryNumber'],item['lotteryNumberSpecial']])
            LotteryPipeline.count += 1
        else:
            writer.writerow([item['turn'],item['dateOpen'],item['dateClose'],item['totalPrize'],item['lotteryNumber'],item['lotteryNumberSpecial']])
            print(item['turn'],item['dateOpen'],item['dateClose'],item['totalPrize'],item['lotteryNumber'],item['lotteryNumberSpecial'],sep='\n')
        return item
