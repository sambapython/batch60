from main import add
import unittest
class AddTests(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		print("this is login section")

	@classmethod
	def tearDownClass(cls):
		print("this is logout section..")
	def setUp(self):
		print("setup")
	def tearDown(self):
		print("teardown")

	def test_add_10_20(self):
		print("test_add_10_20")
		exp=30
		act=add(10,20)
		self.assertEqual(exp, act,"test_add_10_20 failed..")
	def test_add_s1_s2(self):
		print("test_add_s1_s2")
		exp="s1s2"
		act=add("s1","s2")
		self.assertEqual(exp,act,"test_add_s1_s2 failed..")
	def test_add_10_s2(self):
		print("test_add_10_s2")
		exp=None
		act=add(10,"s2")
		self.assertEqual(exp, act, "test_add_10_s2 failed")
	def test_add_s1_20(self):
		print("test_add_s1_20")
		exp=None
		act=add("s1",20)
		self.assertEqual(exp, act, "test_add_s1_20")
unittest.main()