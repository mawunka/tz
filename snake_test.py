import unittest, pyautogui
import unicurses as curses
from snake_d import *

class Test_reset_game(unittest.TestCase):
	def setUp(self):
		pass
	def tearDown(self):
		pass
		
	def test_reset_g(self):
		self.assertEqual(reset_game(), False)

class Test_get_key(unittest.TestCase):

	def setUp(self):
		#self.UP = sys.stdout.write('259')
		#self.DOWN = sys.stdout.write('258')
		#self.LEFT = sys.stdout.write('261')
		#self.RIGHT = sys.stdout.write('260')
		pass
	def tearDown(self):
		pass
		
	def test_get_k1(self):
		
		
		self.assertEqual(get_key(curses.inch()), 10)
	def test_get_k2(self):
		self.assertEqual(get_key(pyautogui.press('enter')), 27)
	def test_get_k3(self):
		self.assertEqual(get_key(pyautogui.press('enter')), 27)
	def test_get_k4(self):
		self.assertEqual(get_key(pyautogui.press('enter')), 27)
		
#class Test_reset_game(unittest.TestCase):
	#def setUp(self):
		#pass
	#def tearDown(self):
		#pass
		
	#def test_snake_coord(self):
		#self.assertEqual(Snake.x, 20)
	
if __name__ == '__main__':
    unittest.main()