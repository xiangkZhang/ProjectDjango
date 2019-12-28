# /usr/bin/evn python
# -*-coding:utf-8 -*-
# Author : XK

from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Chrome()
	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# 访问应用首页

		#访问应用首页
		self.browser.get('http://localhost:8000')

		#网页标题和头部豆瓣汗'To-Do'这个词
		self.assertIn("To-do",self.browser.title)
		self.fail('Finish the test!')


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

if __name__ =="__main__":
	unittest.main(warnings='ignore')