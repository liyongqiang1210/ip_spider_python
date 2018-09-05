# -*- coding: utf-8 -*-


import requests
import telnetlib


if __name__ == '__main__':
	
	response = requests.get('http://www.baidu.com', proxies={'http':'http://36.99.207.98:61234'}, timeout=2)
	print(response.status_code)
	
	try:
		telnetlib.Telnet('111.155.116.196', port='8123', timeout=2)
	except Exception as e:
		print('连接失败')
	else:
		print('连接成功')