# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql


class IpMysqlPipelines(object):

	def process_item(self, item, spider):
		
		# 打开数据连接
		self.conn = pymysql.connect(host='127.0.0.1', user='root',
                password='root', database='maven', charset='utf8')
		# 获取游标对象
		self.cursor = self.conn.cursor()
		
		self.insert_db(item)

		return item

	def insert_db(self, item):
		try:
			# 创建sql语句
			sql = 'INSERT INTO ip_list VALUES (null,"%s","%s","%s","%s","%s","%s","%s")' % (
					item['ip_address'],
					item['ip_port'],
					item['ip_type'],
					item['ip_survival_time'],
					item['ip_verify_time'],
					item['ip_location'],
					item['ip_create_time']
				)
			self.cursor.execute(sql)
			self.conn.commit()
		except Exception as e:
			print('插入数据时发生异常' + e)
			self.conn.rollback()
		finally:
			self.cursor.close()
			self.conn.close()
		
		
	def get_all_ip(self):
		try:
			sql = 'SELECT * FROM ip_list LIMIT 0,1000'
			
			self.cursor.execute(sql)
			results = cursor.fetchall()
			
			for row in results:
				print(row)
		except Exception as e:
			print('查询数据时发生异常' + e)
		finally:
			self.cursor.close()
			self.conn.close()
	
	
