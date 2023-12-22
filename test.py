import unittest
from unittest.mock import patch
import io
from collections.abc import MutableMapping
import prog

class TestAProg(unittest.TestCase):

    def test_arith_prog_sum_with_n_3(self):
        self.assertEqual(prog.a_prog(3), 9)

    def test_arith_prog_sum_with_n_0(self):
        self.assertEqual(prog.a_prog(0), 0)

    def test_arith_prog_sum_with_negative_n(self):
        with self.assertRaises(AssertionError):
            prog.a_prog(-3)

if name == 'main':
    import collections.abc
    import collections
    collections.MutableMapping = collections.abc.MutableMapping
    from xmlrunner import XMLTestRunner

    
    runner = XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    unittest.main()
