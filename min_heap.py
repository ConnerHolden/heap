from random import *
import sys
import getopt

try:
    from binarytree import build
except:
    print("Binarytree package not detected. Tree visualization will not work.")


min_heap = []


def parent(index):
    """For the node at <index>, returns the index of its parent node."""
    parent_index = int(index / 2 if index % 2 == 0 else (index + 1) / 2) - 1
    return parent_index


def bubble_up(index, item):
    """Swaps the <item> node at <index> with its parent node."""
    parent_index = parent(index)
    min_heap.append(min_heap[parent_index])
    min_heap[parent_index] = item
    min_heap[index] = min_heap[-1]
    del min_heap[-1]


def heapify(index, item):
    """Manipulates heap so that the <item> node at <index> is in the right spot."""
    heaped = item >= min_heap[parent(index)]
    while not heaped:
        bubble_up(index, item)
        index = parent(index) if parent(index) != 0 else index
        heaped = item >= min_heap[parent(index)]


def construct_heap():
    """Heapifies entire heap."""
    print("\nConstructing ...\n")
    print("Binary tree: {}".format(min_heap))
    for index, item in enumerate(min_heap[1:], 1):
        heapify(index, item)
    print("Min heap:    {}".format(min_heap))
    print("\nHeap constructed.")


def add_to_heap(item):
    """Adds item to heap and then heapifies it."""
    print("\nAdding ...")
    min_heap.append(item)
    print("Binary tree: {}".format(min_heap))
    heapify(len(min_heap) - 1, item)
    print("Min heap:    {}".format(min_heap))
    print("{} added.".format(item))


def extract_item(index=0):
    """Removes the item at <index> and returns its value."""
    print("\nExtracting ...")
    item = min_heap[index]
    del min_heap[index]
    construct_heap()
    print("Node({}) = {} removed.".format(index, item))


def input_user_choice():
    """Prompt user."""
    user_choice = input("\n>> ").upper()
    return user_choice


def main(argv):
    size = 20
    upper_bound = 100
    global min_heap
    try:
        opts, args = getopt.getopt(argv,"hcs:r:",["size=","range="])
    except getopt.GetoptError:
        print("Error. See 'python min_heap.py -h' for usage.")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("""\nusage: python min_heap.py [-c | --custom] 
                          [-s <value> | --size <value>] [-r <value> | --range <value>]
                                            
Generates random binary tree and constructs a min heap.

    [-c]    Generates an empty array.
    [-s]    Generates random binary tree with <value> items. (Default = 20)
    [-r]    Generates random binary tree of integer values from 1 to <value>. (Default = 100)""")

            sys.exit()
        elif opt in ("-c", "--custom"):
            size = 0
            upper_bound = 0
        elif opt in ("-s", "--size"):
            size = int(arg)
        elif opt in ("-r", "--range"):
            upper_bound = int(arg)
    min_heap = [randint(1, upper_bound) for x in range(size)]  
    construct_heap()

    waiting_for_input = True

    while waiting_for_input:
        print("\n(A)dd item.")
        print("(E)xtract item.")
        print("(O)utput min heap.")
        print("(R)econstruct min heap.")
        print("(V)isualize tree")
        print("(Q)uit")
        user_choice = input_user_choice()
        # Add item
        if user_choice == "A":
            item = int(input("\nItem: "))
            add_to_heap(item)
        # Extract item
        elif user_choice == "E":
            index = int(input("\nIndex: "))
            extract_item(index)
        # Print min heap
        elif user_choice == "O":
            print("Min heap: {}".format(min_heap))
        # Reconstruct min heap
        elif user_choice == "R":
            construct_heap()
        elif user_choice == "V":
            # try:
            tree = build(min_heap)
            print(tree)
            # except:
            #     print("Unknown error.")
        # Quit
        elif user_choice == "Q":
            waiting_for_input = False
        # Invalid entry
        else:
            print("\nInvalid entry.")
    else:
        print("\nUser left!")
        

if __name__ == "__main__":
   main(sys.argv[1:])
