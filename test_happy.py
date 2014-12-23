import unittest
import happy

class TestSquare(unittest.TestCase):
    def setUp(self):
        self.squares = happy.squares

    def test_accuracy(self):
        ''' calculates the squares correctly '''
        for n in xrange(10):
            self.assertEqual(self.squares[str(n)], n**2)

class TestBin_search(unittest.TestCase):
    def setUp(self):
        self.lst = range(1,10)
        self.length = len(self.lst) - 1

    def test_find(self):
        ''' finding elements in the list '''
        for n in (reversed(self.lst)):
            self.assertTrue(happy.bin_search(n, self.lst, 0, self.length))

    def test_not_find(self):
        ''' not finding elements not in the list '''
        for n in range(11, 21):
            self.assertFalse(happy.bin_search(n, self.lst, 0, self.length))

    def test_edge(self):
        ''' index edge cases for binary search '''
        self.assertTrue(happy.bin_search(1, self.lst, 0, 1))
        self.assertTrue(happy.bin_search(1, self.lst, 0, 0))

class TestIs_happy(unittest.TestCase):
    def test(self):
        ''' testing some easy cases for is_happy '''
        self.assertTrue(happy.is_happy(1))
        self.assertFalse(happy.is_happy(2))

if __name__ == '__main__':
    unittest.main()
