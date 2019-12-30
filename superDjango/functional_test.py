# /usr/bin/evn python
# -*-coding:utf-8 -*-
# Author : XK

from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time



class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Chrome()
	def tearDown(self):
		self.browser.quit()
	def check_for_row_in_list_table(self,row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')

		self.assertIn(row_text, [row.text for row in rows])



	def test_can_start_a_list_and_retrieve_it_later(self):
		# 访问应用首页

		#访问应用首页
		self.browser.get('http://localhost:8000')

		#网页标题和头部豆瓣汗'To-Do'这个词
		self.assertIn("To-Do",self.browser.title)

		# 应用邀请他输入一个待办事项
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)
		inputbox.send_keys('Buy peacock feathers')
		inputbox.send_keys(Keys.ENTER)
		time.sleep(3)
		self.check_for_row_in_list_table('Buy peacock feathers')
#他在文本框中输入了'Buy peacock feathers'(购买孔雀羽毛)
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)
		self.check_for_row_in_list_table('Use peacock feathers to make a fly')

#他的爱好是使用假苍蝇做饵钓鱼
#他安乐回车键后，页面更新了
#待办事项表格中展示了"1 Buy peacock feathers"

#页面中又展示了一个文本框，可以输入其它待办事项
#他输入了了"Use peacock "feathers to make a fly"(使用孔雀羽毛做假蝇)
		# inputbox = self.browser.find_element_by_id('id_new_item')
		# inputbox.send_keys('Use peacock feathers to make a fly')
		# inputbox.send_keys(Keys.ENTER)
		# time.sleep(1)
		# # 页面再次更新，清单中显示了这两个待办事项
		# table = self.browser.find_element_by_id('id_list_table')
		# rows = table.find_elements_by_tag_name('tr')
		# self.assertIn('Buy peacock feathers', [row.text for row in rows])

#他做事情很有调理

#页面在此更新，他的清单中展示了这两个待办事项
#他想知道这个网站是否会记住他的清单
#他看到网站为他声称了一个唯一的URL
#而且页面中有一些文字解说这个功能
#他访问那个URL ，发现他的待办事项列表还在
#他很满意，他去睡觉了

if __name__ =="__main__":
	suite = unittest.TestLoader().loadTestsFromTestCase(NewVisitorTest)

	unittest.TextTestRunner(verbosity=2).run(suite)