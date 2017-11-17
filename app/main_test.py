import unittest
import sys
import main as fib_seq

class TestFibSequence(unittest.TestCase):

    def test_fib(self):
        self.assertEqual([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],
                         list(fib_seq._fibonacci(100)))

if __name__ == '__main__':
    unittest.main()
