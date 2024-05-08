import unittest

from data_structure.linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.linked_list = LinkedList()
                
    def test_add(self):
        self.linked_list.add(33)
        self.assertEqual(self.linked_list.tail.data, 33)

    def test_get_by_index(self):
        self.linked_list.add(42)
        item = self.linked_list.get_by_index(0)
        expected = 42
        self.assertEqual(item, expected)

    def test_remove(self):
        self.linked_list.add(3)
        self.linked_list.add(2)
        self.linked_list.add(4)
        self.linked_list.add(13)
        item = self.linked_list.remove(2)
        expected = 4
        self.assertEqual(item, expected)

    def test_insert(self):
        self.linked_list.insert(0, 55)
        item = self.linked_list.get_by_index(0)
        expected = 55
        self.assertEqual(item, expected)
