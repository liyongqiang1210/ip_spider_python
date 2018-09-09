#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-31 16:08:58
# @Author  : Li Yongqiang
# @Version : $Id$

import scrapy
import random
import requests
import time
from ip_spider_python.items import IpItem

class IPSpider(scrapy.Spider):
	"""docstring for IPSpider"""
	#设置name
	name = 'ip'
	#设定域名
	allowed_domains = ['xicidaili.com']
	#填写爬取地址
	start_urls = ['http://www.xicidaili.com/nn']

	def parse(self, response):
		item = IpItem()
		ip_list = response.xpath('//tr')
		for ip in ip_list:
			if ip:
				# 获取ip地址
				item['ip_address'] = ip.xpath('.//td[2]/text()').extract_first()
				# 获取端口号
				item['ip_port'] = ip.xpath('.//td[3]/text()').extract_first()
				# 获取协议类型
				item['ip_type'] = ip.xpath('.//td[6]/text()').extract_first()
				# 获取验证时间
				item['ip_verify_time'] = ip.xpath('.//td[10]/text()').extract_first()
				# 获取存活时间
				item['ip_survival_time'] = ip.xpath('.//td[9]/text()').extract_first()
				# 获取地址
				item['ip_location'] = ip.xpath('.//td[4]/a/text()').extract_first()
				# 爬取时间
				item['ip_create_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		
				# 拼接完整的ip
				ip_address = item['ip_address']
				ip_port = item['ip_port']
				ip_type = 'https'
				if item['ip_type'] == 'HTTP':
					ip_type = 'http'
				proxies = '%s://%s:%s'%(ip_type, ip_address, ip_port)
				
				status = self.verify_ip(ip_type, proxies)
				if status:
					yield item
				else:
					continue

		next_link = response.xpath('//a[@class="next_page"]//@href').extract_first()

		if next_link!= None:
			yield scrapy.Request('http://www.xicidaili.com%s' %(next_link), callback=self.parse)

		time.sleep(random.randint(1,5))

	def verify_ip(slef, ip_type, proxies):
		""" 验证ip可用性 """
		try:
			response = requests.get('https://www.baidu.com/', proxies={str(ip_type):proxies}, timeout=2)
			if response.status_code == 200:
				print(proxies + '====================>可用')
				return True
			else:
				print(proxies + '====================>不可用')
		except Exception as e:
			print('请求失败,ip地址：' + proxies)
			
		return False
		


