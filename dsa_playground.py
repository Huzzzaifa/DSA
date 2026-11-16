"""Small implementations of foundational data structures and algorithms."""

from collections import deque
from typing import Deque, Dict, Generic, List, Optional, TypeVar

T = TypeVar("T")


class Stack(Generic[T]):
    """A last-in, first-out collection."""

    def __init__(self) -> None:
        self._items: List[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def is_empty(self) -> bool:
        return not self._items


class Queue(Generic[T]):
    """A first-in, first-out collection."""

    def __init__(self) -> None:
        self._items: Deque[T] = deque()

    def enqueue(self, item: T) -> None:
        self._items.append(item)

    def dequeue(self) -> T:
        if not self._items:
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    def is_empty(self) -> bool:
        return not self._items


def binary_search(values: List[int], target: int) -> int:
    """Return target's index in a sorted list, or -1 when it is absent."""
    low, high = 0, len(values) - 1
    while low <= high:
        middle = (low + high) // 2
        if values[middle] == target:
            return middle
        if values[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1


def merge_sort(values: List[int]) -> List[int]:
    """Return a sorted copy of values using merge sort."""
    if len(values) < 2:
        return values.copy()

    middle = len(values) // 2
    left = merge_sort(values[:middle])
    right = merge_sort(values[middle:])
    merged: List[int] = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged


def shortest_path(
    graph: Dict[str, List[str]], start: str, goal: str
) -> Optional[List[str]]:
    """Find a shortest path in an unweighted graph, or return None."""
    if start not in graph or goal not in graph:
        return None

    pending = deque([start])
    previous: Dict[str, Optional[str]] = {start: None}

    while pending:
        node = pending.popleft()
        if node == goal:
            path: List[str] = []
            cursor: Optional[str] = node
            while cursor is not None:
                path.append(cursor)
                cursor = previous[cursor]
            return list(reversed(path))

        for neighbor in graph.get(node, []):
            if neighbor not in previous:
                previous[neighbor] = node
                pending.append(neighbor)

    return None


def main() -> None:
    stack: Stack[int] = Stack()
    stack.push(10)
    stack.push(20)

    queue: Queue[str] = Queue()
    queue.enqueue("first")
    queue.enqueue("second")

    graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D"],
        "D": [],
    }

    print("Stack pop:", stack.pop())
    print("Queue dequeue:", queue.dequeue())
    print("Binary search for 7:", binary_search([1, 3, 5, 7, 9], 7))
    print("Merge sort:", merge_sort([8, 3, 5, 1, 9]))
    print("Shortest path A -> D:", shortest_path(graph, "A", "D"))


if __name__ == "__main__":
    main()
