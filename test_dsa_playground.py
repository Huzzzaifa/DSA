import unittest

from dsa_playground import (
    Queue,
    Stack,
    binary_search,
    merge_sort,
    shortest_path,
)


class DataStructureTests(unittest.TestCase):
    def test_stack_is_last_in_first_out(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertTrue(stack.is_empty())

    def test_pop_empty_stack_raises(self):
        with self.assertRaises(IndexError):
            Stack().pop()

    def test_queue_is_first_in_first_out(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)
        self.assertTrue(queue.is_empty())

    def test_dequeue_empty_queue_raises(self):
        with self.assertRaises(IndexError):
            Queue().dequeue()


class AlgorithmTests(unittest.TestCase):
    def test_binary_search_finds_value_and_handles_missing_value(self):
        self.assertEqual(binary_search([1, 3, 5, 7], 5), 2)
        self.assertEqual(binary_search([1, 3, 5, 7], 4), -1)
        self.assertEqual(binary_search([], 4), -1)

    def test_merge_sort_sorts_without_changing_input(self):
        values = [5, 2, 8, 2, -1]
        self.assertEqual(merge_sort(values), [-1, 2, 2, 5, 8])
        self.assertEqual(values, [5, 2, 8, 2, -1])

    def test_shortest_path(self):
        graph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
        self.assertEqual(shortest_path(graph, "A", "D"), ["A", "B", "D"])
        self.assertEqual(shortest_path(graph, "A", "A"), ["A"])
        self.assertIsNone(shortest_path(graph, "D", "A"))
        self.assertIsNone(shortest_path(graph, "missing", "A"))


if __name__ == "__main__":
    unittest.main()
