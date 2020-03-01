import unittest


class B(unittest.TestCase):
    def setUp(self):
        self.x = 3
        self.y = 4

    def test_1(self):
        self.assertEqual(self.x+self.y, 7)
        print("\nB.test_1")

    def test_2(self):
        self.assertEqual(self.y - self.x, 1)
        print("\nB.test_2")

    def tearDown(self):
        pass


class C(unittest.TestCase):
    def setUp(self):
        self.x = 3
        self.y = 4

    def test_7(self):
        self.assertEqual(self.x+self.y, 7)
        print("\nB.test_1")

    def tearDown(self):
        pass


if __name__ == "__main":
    unittest.main()
