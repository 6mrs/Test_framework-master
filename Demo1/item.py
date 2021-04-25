# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Demo1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    manufacturer = scrapy.Field()
    ranking = scrapy.Field()
    vehicle_type = scrapy.Field()
    monthly_sales_volume = scrapy.Field()
    accumulated_this_year = scrapy.Field()
    last_month = scrapy.Field()
    chain_ratio = scrapy.Field()
    corresponding_period_of_last_year = scrapy.Field()
    year_on_year = scrapy.Field()
    url_title = scrapy.Field()
    month = scrapy.Field()
    # url_href = scrapy.Field()
    series = scrapy.Field()
    url_car_detail = scrapy.Field()

    pass