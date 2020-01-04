from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.models import Item,List
import unittest


# Create your tests here.
class SmokeTest(TestCase):

	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func,home_page)
	def test_home_page_returns_correct_html(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response,'home.html')

	# def test_can_save_a_POST_request(self):
	# 	response = self.client.post('/',data={'item_text':'A new list item'})
	# 	self.assertEqual(Item.objects.count(),1)
	# 	new_item = Item.objects.first()
	# 	self.assertEqual(new_item.text,'A new list item')


	# def test_redirects_after_POST(self):
	# 	response = self.client.post('/', data={'item_text':'A new list item'})
	# 	self.assertEqual(response.status_code, 302)
	# 	self.assertEqual(response['location'], '/lists/the-only-list-in-the-world/')
	#
	# 	self.assertIn('A new list item',response.content.decode())
	# 	self.assertTemplateUsed(response,'home.html')
class ListAndItemModelsTest(TestCase):
	def test_saving_and_retrieving_items(self):
		list_ =List()
		list_.save()
		first_item=Item()
		first_item.text = 'This first (even) list item'
		first_item.list = list_
		first_item.save()

		second_item = Item()
		second_item.text = 'Item the second'
		second_item.list = list_
		second_item.save()
		saved_list = List.objects.first()
		self.assertEqual(saved_list, list_)
		saved_list = List.objects.first()
		self.assertEqual(saved_list, list_)
		save_items = Item.objects.all()
		self.assertEqual(save_items.count(),2)
		first_save_item = save_items[0]
		second_save_item = save_items[1]
		self.assertEqual(first_save_item.list, list_)
		self.assertEqual(second_save_item.list, list_)
		self.assertEqual(first_save_item.text,'This first (even) list item')
		self.assertEqual(second_save_item.text,'Item the second')


class ListViewTest(TestCase):

	def test_display_all_items(self):
		Item.objects.create(text='item1')
		Item.objects.create(text='item2')

		response = self.client.get('/lists/the-only-list-in-the-world/')
		self.assertContains(response,'item1')
		self.assertContains(response,'item2')

	def test_uses_list_template(self):
		response= self.client.get('/lists/the-only-list-in-the-world/')
		self.assertTemplateUsed(response,'list.html')

	def test_can_save_a_POST_request(self):
		self.client.get('/lists/new',data={'item_text':'A new list item'})
		self.assertEqual(Item.objects.count(),1)
		new_item =Item.objects.first()
		self.assertEqual(new_item.text,'A new list item')

	def test_redirects_after_POST(self):
		response = self.client.get('/lists/new',data={'item_text':'A new list item'})
		self.assertEqual(response.status_code,302)
		self.assertEqual(response['loaction'],'/lists/the-only-list-in-the-world/')
		self.assertRedirects(response,'/lists/the-only-list-in-the-world/')

	def test_passes_correct_list_to_template(self):
		other_list = List.objects.create()

		correct_list = List.objects.create()
		response = self.client.get(f'/lists/{correct_list.id}/')
		self.assertEqual(response.context['list'], correct_list)
