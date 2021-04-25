import scrapy
from Demo1.items import Demo1Item
from scrapy.http import Request
from scrapy.selector import Selector


class UestcInfoSpider(scrapy.spiders.Spider):
    # 爬虫名
    name = 'uestc'
    # 设置访问域
    allowed_domains = ['ecar168.cn']
    # 网页链接、
    # start_urls = ['http://data.ecar168.cn/car/959/']
    start_urls = ['http://www.ecar168.cn/xiaoliang/liebiao/60_0.htm']

    def parse1(self, response):
        item = Demo1Item()
        selector = Selector(response)
        news1 = selector.xpath('(//tr[@class="yuefen_tr"])')
        for each in news1:
            item['ranking'] = each.xpath('normalize-space(td[1]/text())').extract()[0]
            item['manufacturer'] = each.xpath('normalize-space(td[2]/text())').extract()[0]
            item['vehicle_type'] = each.xpath('normalize-space(td[3]/text())').extract()[0] + \
                                   each.xpath('normalize-space(td[3]/a/text())').extract()[0]
            item['monthly_sales_volume'] = each.xpath('normalize-space(td[4]/text())').extract()[0]
            item['accumulated_this_year'] = each.xpath('normalize-space(td[5]/text())').extract()[0]
            item['last_month'] = each.xpath('normalize-space(td[6]/text())').extract()[0]
            item['chain_ratio'] = each.xpath('normalize-space(td[7]/text())').extract()[0]
            item['corresponding_period_of_last_year'] = each.xpath('normalize-space(td[8]/text())').extract()[0]
            item['year_on_year'] = each.xpath('normalize-space(td[9]/text())').extract()[0]
            item['url_title'] = selector.xpath('//div[@id="left"]/div[1]/div[2]/h1/text()').extract()[0]
            # date1= selector.xpath('//div[@id="left"]/div[1]/div[2]/h1/text()').extract()[0]
            # item['month'] = (selector.xpath('//div[@id="left"]/div[1]/div[3]/text()').extract()[0])[3:10]
            # item['web'] = selector.xpath('//div[@id="left"]/div[1]/div[1]/a[3]').extract()[0]
            # item['url_href'] = selector.xpath('//div[@id="left"]/div[1]/div[1]/a[1]//@href').extract()[0] + selector.xpath('//div[@id="left"]/div[1]/div[1]/a[3]//@href').extract()[0]
            series = (selector.xpath('//div[@id="left"]/div[1]/div[2]/h1/text()').extract()[0])
            begin = series.find("月")
            end = series.find("车")
            seriestest = series[begin + 1:end]
            item['series'] = seriestest

            item['url_car_detail'] = each.xpath('normalize-space(td[3]/a/@href)').extract()[0]
            monthdan = selector.xpath('//div[@id="left"]/div[1]/div[2]/h1/text()').extract()[0][0:7]

            if monthdan.find("月") == -1:
                month = monthdan + "月"

            else:
                month = monthdan
            item['month'] = month

            yield item

    def parse2(self, response):
        item = Demo1Item()
        selector = Selector(response)
        news = selector.xpath('(//ul[@class="biaoti_ul"])')
        for each in news:
            url2 = 'http://www.ecar168.cn' + each.xpath('normalize-space(li[1]/a/@href)').extract()[0]
            print(url2)
            yield Request(url2, callback=self.parse1)

    def parse(self, response):
        # 创建item
        item = Demo1Item()
        # 分析response
        selector = Selector(response)
        news = selector.xpath('(//div[@id="jiludaohang"])')
        # i=0
        # while i <=180:
        # url=["http://www.ecar168.cn/xiaoliang/liebiao/60_%s.htm"%i]
        # print(url)
        # url='http://www.ecar168.cn/xiaoliang/liebiao/60_0.htm'
        for each in news:
            for i in range(3, 9):
                url = 'http://www.ecar168.cn' + each.xpath('ul/li[%s]/a/@href' % i).extract()[0]
                print(url)
                yield Request(url, callback=self.parse2)
