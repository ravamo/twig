import unittest
import Tiwg

class UnitTestTwig(unittest.TestCase):

    def test_check_empty_list(self):
        self.assertEqual(Tiwg.twig.check([], 3), [])

    def test_check_list(self):
        self.assertEqual(Tiwg.twig.check([1, 2, 3, 4, 5, 6] ,3), True)

    def test_check_list_chunk(self):
        self.assertEqual(Tiwg.twig.check([1, 2, 3, 4, 5, 6] ,-3), False)

    def test_chunks_positive(self):
        self.assertEqual(Tiwg.twig.groupArrayElements([1,2] ,-3), None)

    def test_list_elements_positive(self):
        self.assertEqual(Tiwg.twig.groupArrayElements([] ,3), None)

    def test_value_one(self):
        self.assertEqual(Tiwg.twig.groupArrayElements([1] ,6), [[1], [ ], [ ], [ ], [ ], []])

    def test_value(self):
        self.assertEqual(Tiwg.twig.groupArrayElements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13], 6),
                         [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13], []])

    def test_value_even(self):
        self.assertEqual(Tiwg.twig.groupArrayElements([1, 2, 3, 4, 5, 6] ,3), [[1, 2], [3, 4], [5, 6]])

    def test_value_odd(self):
        self.assertEqual(Tiwg.twig.groupArrayElements([1, 2, 3, 4, 5] ,3), [[1, 2], [3, 4], [5]])

if __name__ == '__main__':
    unittest.main()