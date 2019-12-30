from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.models import Item



# Create your tests here.
class SmokeTest(TestCase):

	# def test_root_url_resolves_to_home_page_view(self):
	# 	found = resolve('/')
	# 	self.assertEqual(found.func,home_page)
	# def test_home_page_returns_correct_html(self):
	# 	response = self.client.get('/')
	# 	self.assertTemplateUsed(response,'home.html')

	def test_can_save_a_POST_request(self):
		response = self.client.post('/',data={'item_text':'A new list item'})
		self.assertEqual(Item.objects.count(),1)
		new_item = Item.objects.first()
		self.assertEqual(new_item.text,'A new list item')


	def test_redirects_after_POST(self):
		response = self.client.post('/', data={'item_text':'A new list item'})
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/')

		# self.assertIn('A new list item',response.content.decode())
		# self.assertTemplateUsed(response,'home.html')
# class ItemModleTest(TestCase):
# 	def test_saving_and_retrieving_items(self):
# 		first_item=Item()
# 		first_item.text = 'This first (even) list item'
# 		first_item.save()
#
# 		second_item = Item()
# 		second_item.text = 'Item the second'
# 		second_item.save()
#
# 		save_items = Item.objects.all()
# 		self.assertEqual(save_items.count(),2)
# 		first_save_item = save_items[0]
# 		second_save_item = save_items[1]
# 		self.assertEqual(first_save_item,'This first (even) list item')
# 		self.assertEqual(second_save_item,'Item the second')

	def test_display_all_list_items(self):
		Item.objects.create(text='item1')
		Item.objects.create(text='item2')
		response= self.client.get('/')
		self.assertIn('item1',response.content.decode())
		self.assertIn('item2',response.content.decode())