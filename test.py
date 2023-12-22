import unittest
import prog

class TestAProg(unittest.TestCase):

    def test_arith_prog_sum_with_n_3(self):
        self.assertEqual(prog.a_prog(3), 9)

    def test_arith_prog_sum_with_n_0(self):
        self.assertEqual(prog.a_prog(0), 0)

    def test_arith_prog_sum_with_negative_n(self):
        with self.assertRaises(AssertionError):
            prog.a_prog(-3)

if __name__ == "__main__":
    from xmlrunner import XMLTestRunner

    runner = XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)

    unittest.main()

