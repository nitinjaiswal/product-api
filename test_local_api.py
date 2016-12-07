import unittest
from flask.ext.testing import TestCase
import app

import requests
username = 'nitin'
password = 'nitin'
url = 'http://localhost:5000/wingify/api/v1.0/product/'


class FlaskTestCase(unittest.TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		url1 = url + "P1010"
		res = requests.delete(url1, auth=(username, password))

	def create_app(self):
		app.config["TESTING"] = True
		app.config["LIVESERVER_TIMEOUT"] = 10




	def test_unauthorization(self):
		res = requests.get(url)
		self.assertEqual(res.status_code, 401)


	def test_authorization(self):

		res = requests.get(url, auth=(username, password))
		self.assertEqual(res.status_code, 200)

	def test_get_product(self):
		res = requests.get(url, auth=(username, password))
		self.assertEqual(res.status_code, 200)
		print(res.json())

	def test_get_one_product(self):
		url1 = url + "P1000"
		res = requests.get(url1, auth=(username, password))
		self.assertEqual(res.status_code, 200)
		print(res.json())

	def test_post_product(self):

		data = {'pid': 'P1010', 'name':"xyz",'desccription':"xyz",'supplier_name':"xyz", 'status':"xyz",'price':"xyz"}
		res = requests.post(url, json=data, auth=(username, password))
		self.assertEqual(res.status_code, 200)
		print(res.json())

	def test_update_product(self):
		url1 = url + "P1010"
		data = {'pid': 'P1010', 'name': "updated_xyz", 'desccription': "updated_xyz", 'supplier_name': "updated_xyz", 'status': "updated_xyz",'price': "updated_xyz"}
		res = requests.post(url1, json=data, auth=(username, password))
		self.assertEqual(res.status_code, 200)
		print(res.json())

	def test_delete_product(self):
		url1 = url + "P1010"
		res = requests.delete(url1, auth=(username, password))
		self.assertEqual(res.status_code, 200)
		print(res.json())








if __name__ == '__main__':
	unittest.main()


