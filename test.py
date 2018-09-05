# -*- coding: utf-8 -*-


import requests
import pymysql
import time
import random


def read_html(ip_list):

	user_agent_list = [
			'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
			'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
			'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
			'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
			'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
			'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
			'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
			'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
			'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
			'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
			'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
			'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
		]

	for i in range(20):
		ip_obj = random.choice(ip_list)
		ip_id = ip_obj[0]
		ip_address = ip_obj[1]
		ip_port = ip_obj[2]
		ip_type = ip_obj[3]
		time.sleep(5)
		# 开始读取页面
		try:
			print('%s://%s:%s===================>可用'%(ip_type, ip_address, ip_port))
			
			# 随机获取user-agent
			user_agent = random.choice(user_agent_list)
			headers ={
				'User-Agent': user_agent,
				'Content-Type': 'application/json; charset=UTF-8',
				'Accept': r'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
				'Host': 'blog.csdn.net',
				'Referer': r'https://www.csdn.net/nav/newarticles'
				}
			response = requests.get('https://blog.csdn.net/wl_Honest/article/details/82426753', 
				proxies={'%s'%(ip_type):'%s://%s:%s'%(ip_type, ip_address, ip_port)}, headers=headers, timeout=2)
			print(response.status_code)
			# print(response.text)

		except Exception as e:
			print('%s://%s:%s====================>不可用'%(ip_type, ip_address, ip_port))
			continue
		

def read_ip():
	ip_list = []
	try:
		# 从数据库获取ip地址
		conn = pymysql.connect(host='127.0.0.1', user='root',
				password='root', database='lyq_db', charset='utf8')
		# 获取游标对象
		cursor = conn.cursor()
		sql = 'SELECT * FROM ip_list LIMIT 0,1000'
		cursor.execute(sql)
		results = cursor.fetchall()
		for row in results:
			ip_list.append(row)
	except Exception as e:
		print('出现异常')
	finally:
		cursor.close()
		conn.close()

	return ip_list

if __name__ == '__main__':
	
	ip_list = read_ip()
	read_html(ip_list)

	
