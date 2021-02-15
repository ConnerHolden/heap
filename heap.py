# min_heap = [None] * 5
from random import *


min_heap = [randint(1, 100) for x in range(6)]
queue_end = len(min_heap)


def parent(position):
    parent_index = int(position / 2 if position % 2 == 0 else (position - 1) / 2) - 1
    return parent_index


def bubble_up(item):
    min_heap.append(min_heap[parent(queue_end)])
    min_heap[parent(queue_end)] = item


def add_to_queue(item):
    heaped = item < min_heap[parent(queue_end)]
    while not heaped:
        bubble_up(item)
    else:
        min_heap.append(item)


def remove_from_queue():
    pass


add_to_queue(1)
print(min_heap)