from random import *


min_heap = [randint(1, 100) for x in range(20)]


def parent(position):
    index = int(position / 2 if position % 2 == 0 else (position + 1) / 2) - 1
    return index


def bubble_up(index, item):
    parent_index = parent(index)
    min_heap.append(min_heap[parent_index])
    min_heap[parent_index] = item
    min_heap[index] = min_heap[-1]
    del min_heap[-1]


def heapify(index, item):
    heaped = item >= min_heap[parent(index)]
    while not heaped:
        bubble_up(index, item)
        index = parent(index) if parent(index) != 0 else index
        heaped = item >= min_heap[parent(index)]


def initialize_heap():
    for index, item in enumerate(min_heap[1:], 1):
        heapify(index, item)


def add_to_heap(item):
    min_heap.append(item)
    heapify(len(min_heap) - 1, item)


def extract_item(index=0):
    item = min_heap[index]
    del min_heap[index]
    initialize_heap()
    return item


print(min_heap)
initialize_heap()
print(min_heap)
add_to_heap(1)
print(min_heap)
extract_item()
print(min_heap)

