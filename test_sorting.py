import unittest
from Sorting_Algorithm.quick_sort import Sorting

class TestQuickSort(unittest.TestCase):
    def setUp(self):
        self.quick_sort = Sorting()

    def test_sort_unsorted_array(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        result = self.quick_sort.quicksort(arr)
        self.assertEqual(result, [1, 1, 2, 3, 6, 8, 10])

    def test_sort_empty_array(self):
        arr = []
        result = self.quick_sort.quicksort(arr)
        self.assertEqual(result, [])

    def test_sort_single_element(self):
        arr = [5]
        result = self.quick_sort.quicksort(arr)
        self.assertEqual(result, [5])

    def test_sort_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        result = self.quick_sort.quicksort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5])

if __name__ == "__main__":
    unittest.main()