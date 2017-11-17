import unittest
import tempfile
import os
import sys
sys.path.insert(0, './fib-sequence-generator/')
import main as fib_seq

class TestFibSequence(unittest.TestCase):

    def setUp(self):
        fib_seq.app.testing = True
        self.app = fib_seq.app.test_client()

    def test_fib(self):
        self.assertEqual([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],
                         list(fib_seq._fibonacci(100)))

    def test_index(self):
        rv = self.app.get('/')
        assert b'Input number to generate sequence up to' in rv.data

    def test_fib_sequence_to_100(self):
        rv = self.app.get('/fib-generator?fib-max-number=100')
        assert b'[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]' in rv.data

    def test_fib_sequence_to_non_int(self):
        rv = self.app.get('/fib-generator?fib-max-number=100afsd')
        assert b"Not an integer!" in rv.data

    def test_fib_sequence_to_non_int_with_symbols(self):
        rv = self.app.get('/fib-generator?fib-max-number=100afsd!@#')
        assert b"Not an integer!" in rv.data

    def test_fib_sequence_decimal_given(self):
        rv = self.app.get('/fib-generator?fib-max-number=10.2')
        assert b"Not an integer!" in rv.data

    def test_fib_sequence_negative_number_given(self):
        rv = self.app.get('/fib-generator?fib-max-number=-100')
        assert b"Must provide a number greater than 0" in rv.data

    def test_fib_sequence_negative_number_given(self):
        rv = self.app.get('/fib-generator?fib-max-number=-100')
        assert b"Must provide a number greater than 0" in rv.data

if __name__ == '__main__':
    unittest.main()
