import unittest


class testhaha(unittest.TestCase):
    def setUp(self):
        self.x = 3
        self.y = 4

    def test_3(self):
        self.assertEqual(self.x+self.y, 7)
        print("\nA.test_3")

    def test_4(self):
        self.assertEqual(self.y + self.x, 1)
        print("\nA.test_4")

    def tearDown(self):
        pass

if __name__ == "__main":
   unittest.main()