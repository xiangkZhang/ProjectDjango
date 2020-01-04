# /usr/bin/evn python
# -*-coding:utf-8 -*-
# Author : XK
from django.test import LiveServerTestCase
from selenium import webdriver
import time
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(LiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Chrome()
	def tearDown(self):
		self.browser.quit()



	def wait_for_row_in_list_table(self,row_text):
		Max_Wait = 10
		start_time = time.time()
		while True:
			try:
				self.browser.find_element_by_id('id_list_table')
				rows =self.browser.find_elements_by_tag_name('tr')
				self.assertIn(row_text,[row.text for row in rows])
				return
			except (AssertionError,WebDriverException) as e:
				if time.time()-start_time> Max_Wait:
					raise e
				time.sleep(0.5)




	def test_can_start_a_list_and_retrieve_it_later(self):
		# 访问应用首页

		#访问应用首页
		self.browser.get(self.live_server_url)

		#网页标题和头部豆瓣汗'To-Do'这个词
		self.assertIn("To-Do",self.browser.title)
		# self.fail('Finish the test!')
		input1 =self.browser.find_element_by_id('id_new_item')
		input1.send_keys('Buy peacock feathers')
		input1.send_keys(Keys.ENTER)

		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)

		self.wait_for_row_in_list_table('1:Buy peacock feathers')
		self.wait_for_row_in_list_table('2:Use peacock feathers to make a fly')

	def test_multiple_users_can_start_lists_at_diffrent_urls(self):
		self.browser.get(self.live_server_url)
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Buy peacock feathers')
		inputbox.send_keys(Keys.ENTER)

		edith_list_url = self.browser.current_url
		self.assertRegex(edith_list_url,'/lists/.+')


#应用邀请他输入一个待办事项
#他在文本框中输入了'Buy peacock feathers'(购买孔雀羽毛)
#他的爱好是使用假苍蝇做饵钓鱼
#他安乐回车键后，页面更新了
#待办事项表格中展示了"1 Buy peacock feathers"

#页面中又展示了一个文本框，可以输入其它待办事项
#他输入了了"Use peacock "feathers to make a fly"(使用孔雀羽毛做假蝇)

#他做事情很有调理

#页面在此更新，他的清单中展示了这两个待办事项
#他想知道这个网站是否会记住他的清单
#他看到网站为他声称了一个唯一的URL
#而且页面中有一些文字解说这个功能
#他访问那个URL ，发现他的待办事项列表还在
#他很满意，他去睡觉了
