# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IpItem(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()

	# ip地址
	ip_address = scrapy.Field()
	# ip端口号
	ip_port = scrapy.Field()
	# ip类型
	ip_type = scrapy.Field()
	# ip存活时间
	ip_survival_time = scrapy.Field()
	# ip验证时间
	ip_verify_time = scrapy.Field()
	# ip真实地址(省市)
	ip_location = scrapy.Field()
	# 爬取时间
	ip_create_time = scrapy.Field()
