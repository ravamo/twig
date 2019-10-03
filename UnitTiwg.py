import unittest
import Tiwg

class UnitTestTwig(unittest.TestCase):

    def test_check_empty_list(self):
        self.assertEqual(Tiwg.twig.check([], 3), [])

    def test_check_list(self):
        self.assertEqual(Tiwg.twig.check([1, 2, 3, 4, 5, 6] ,3), True)

    def test_check_list_chunk(self):
        self.assertEqual(Tiwg.twig.check([1, 2, 3, 4, 5, 6] ,-3), False)

    def test_value_even(self):
        self.assertEqual(Tiwg.twig.groupArrayElements([1, 2, 3, 4, 5, 6] ,3), [[1, 2], [3, 4], [5, 6]])

    def test_value_odd(self):
        self.assertEqual(Tiwg.twig.groupArrayElements([1, 2, 3, 4, 5] ,3), [[1, 2], [3, 4], [5]])

    def test_chunks_positive(self):
        self.assertEqual(Tiwg.twig.groupArrayElements([1,2] ,-3), None)

    def test_list_elements_positive(self):
        self.assertEqual(Tiwg.twig.groupArrayElements([] ,3), None)


    #def test_value_even(self):
    #    self.assertEqual(Tiwg.twig.groupArrayElementsAlternative([1, 2, 3, 4, 5, 6], 3), [[1, 2], [3, 4], [5, 6]])

    #def test_value_odd(self):
    #    self.assertEqual(Tiwg.twig.groupArrayElementsAlternative([1, 2, 3, 4, 5], 3), [[1, 2], [3, 4], [5]])

    #def test_chunks_positive(self):
    #    self.assertEqual(Tiwg.twig.groupArrayElementsAlternative([1, 2], -3), None)

    #def test_list_elements_positive(self):
    #    self.assertEqual(Tiwg.twig.groupArrayElementsAlternative([], 3), None)

if __name__ == '__main__':
    unittest.main()