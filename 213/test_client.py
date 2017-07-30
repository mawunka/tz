import unittest
from c_v2 import client


class TestClient(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test0(self):
        self.assertEqual(client(2000, False, 'test0', None), '[done]')

    def test1(self):
        self.assertEqual(client(2000, False, 'test1', None), '[done]')

    def test2(self):
        self.assertEqual(client(2000, False, 'test2', None), '[done]')

    def test3(self):
        self.assertEqual(client(2000, True, None, '1'), 'test2\n'
                                                       '[done]')

    def test4(self):
        self.assertEqual(client(2000, True, None, None), 'test1\n'
                                                        '[done]')
	def test4(self):
        self.assertEqual(client(2000, True, None, None), 'test0\n'
                                                        '[done]')


    def test5(self):
        self.assertEqual(client(2000, False, 'asd', '12000'), p.print_help())

    def test6(self):
        self.assertEqual(client(), p.print_help())



if __name__ == '__main__':
    unittest.main()