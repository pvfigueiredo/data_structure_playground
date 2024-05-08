import unittest
import random

from sort_algorithm.merge_sort import MergeSort

class TestMergeSort(unittest.TestCase):
    def test_array_size_2(self):
        arr = [2,1]
        MergeSort.sort(arr)
        self.assertEqual(arr, [1,2])
    
    def test_array_size_3(self):
        arr = [3, 2, 1]
        MergeSort.sort(arr)
        self.assertEqual(arr, [1, 2, 3])

    def test_array_size_4(self):
        arr = [2, 4, 1, 3]
        MergeSort.sort(arr)
        self.assertEqual(arr, [1,2,3,4])

    def test_array_size_n(self):
        random.seed()
        n = random.randint(0, 100)
        arr = [random.randint(0, 1000) for i in range(n)]
        arr2 = arr.copy()
        arr2.sort()
        MergeSort.sort(arr)
        self.assertEqual(arr, arr2)