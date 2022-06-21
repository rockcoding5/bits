# Import required Python Native Imports
import os
import sys


def read_input_file(input_file):
    """
    This function reads the given input file (input*.txt) and return List with list of Integer entries
    [start point, checkout time]
    :param input_file:
    :return: list[list[]]
    """
    try:
        with open(os.path.join('', input_file), 'r') as input_file:
            lines = input_file.readlines()
            if len(lines) == 0:
                print('Input file is Empty! Please check')
            else:
                input_list = []
                try:
                    for line in lines:
                        input_temp = line.rstrip('\n').strip("'[]'").replace(' ', '').split(',')
                        input_list.append([int(input_temp[0]), int(input_temp[1])])
                    # print(input_list)
                except:
                    print(f"Incorrect format of input dataset. Expected e.g '[0, 1]' in each line ")
                    print(f"Exiting the program!")
                    sys.exit()
        return input_list
    except FileNotFoundError:  # Handle the File not found error
        print(input_file + ' Input file not found! Please check')
        exit()
    except:  # Handle any other error
        print(input_file + ' Cannot Read input file! Please check')
        exit()


def cleanup_output_file(output_file):
    """
    This function just clean up the output file (output*.txt) if exists
    :param output_file:
    :return: None
    """
    # Current folder is parent folder
    if os.path.isfile(os.path.join('', output_file)):
        os.remove(os.path.join('', output_file))


def write_output(output_file, to_write):
    """
    This function just writes the text given to it in the output file (output*.txt)
    :param output_file:
    :param to_write:
    :return: None
    """
    to_write = 'Minimum Checkout counters required: ' + str(to_write)
    # print(to_write)
    with open(output_file, 'a+') as outf:
        outf.write(to_write)


def cust_heapify(input_list, element, i):
    """
    This function just writes the text given to it in the output file (output*.txt)
    :param input_list:
    :param element:
    :param i:
    :return: List
    """
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < element and input_list[i] < input_list[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < element and input_list[largest] < input_list[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        input_list[i], input_list[largest] = input_list[largest], input_list[i]  # swap

        # Heapify the root.
        cust_heapify(input_list, element, largest)


def cust_heap_sort(input_list):
    """
    This function to sort a List of given size, using Custom HeapSort implementation
    :param input_list:
    :return: List
    """
    length = len(input_list)

    # Build a minheap.
    # Since last parent will be at ((n//2)-1) we can start at that location.
    for elem in range(length // 2 - 1, -1, -1):
        cust_heapify(input_list, length, elem)

    # One by one extract elements
    for elem in range(length - 1, 0, -1):
        input_list[elem], input_list[0] = input_list[0], input_list[elem]  # swap
        # here i=0. assumption that largest is zero ie: 0
        cust_heapify(input_list=input_list, element=elem, i=0)

    return input_list


def shift_up_with_parent(heap, pos):
    """
    This function to Shift up the Element with Parent
    :param heap:
    :param pos:
    :return: List
    """
    end_pos = len(heap)
    start_pos = pos
    new_item = heap[pos]
    # Bubble up the smaller child until hitting a leaf.
    child_pos = 2 * pos + 1  # leftmost child position
    while child_pos < end_pos:
        # Set child_pos to index of smaller child.
        right_pos = child_pos + 1
        if right_pos < end_pos and not heap[child_pos] < heap[right_pos]:
            child_pos = right_pos
        # Move the smaller child up.
        heap[pos] = heap[child_pos]
        pos = child_pos
        child_pos = 2 * pos + 1
    # The leaf at pos is empty now.  Put new_item there, and bubble it up
    # to its final resting place (by sifting its parents down).
    heap[pos] = new_item
    shift_down_with_child(heap, start_pos, pos)


def shift_down_with_child(heap, start_pos, pos):
    """
    This function to Shift down the Element with Child
    :param heap:
    :param start_pos:
    :param pos:
    :return: List
    """
    new_item = heap[pos]
    # Follow the path to the root, moving parents down until finding a place
    # new_item fits.
    while pos > start_pos:
        parent_pos = (pos - 1) >> 1
        parent = heap[parent_pos]
        if new_item < parent:
            heap[pos] = parent
            pos = parent_pos
            continue
        break
    heap[pos] = new_item


def cust_heap_push(heap, item):
    """
    This function to Push item onto heap, maintaining the heap invariant.
    :param heap:
    :param item:
    :return: List
    """
    heap.append(item)
    shift_down_with_child(heap, 0, len(heap) - 1)


def cust_heap_push_pop(heap, item):
    """
    This function to implement heappush followed by a heappop.
    :param heap:
    :param item:
    :return: item
    """
    if heap and heap[0] < item:
        item, heap[0] = heap[0], item
        shift_up_with_parent(heap, 0)
    return item


def min_counters(intervals):
    """
    This function to find minimum checkout counters required
    :param intervals:
    :return: int
    """
    counters = 0
    checkout_counter_list = []
    for interval in intervals:
        if not checkout_counter_list:
            checkout_counter_list.append(interval[1])
            # Increment Counters by one
            counters += 1
        else:
            if interval[0] >= checkout_counter_list[0]:
                # Custom Heap Push and Pop logic method
                cust_heap_push_pop(checkout_counter_list, interval[1])  # pop the first heap element
            else:
                # Custom Heap Push logic method
                cust_heap_push(checkout_counter_list, interval[1])
                # Increment Counters by one
                counters += 1
    return counters


def get_end_time(input_list):
    """
    This function to calculate the End time by using start time and required checkout time
    :param input_list:
    :return: List
    """
    start_end_time = []
    for il in input_list:
        start_end_time.append([il[0], (il[0]) + il[1]])
        # print(start_end_time)
    return start_end_time


if __name__ == '__main__':
    # Initialize the Paths. Current folder is parent folder

    input_file_name = 'inputPS10.txt'
    output_file_name = 'outputPS10.txt'

    # Read the Input file and create a List with list of Integer entries [start point, checkout time]
    input_file_list = read_input_file(input_file=input_file_name)
    # print('Input File List : ' + str(input_file_list))

    # Calculate the End time by using start time and required checkout time
    start_end_intervals = get_end_time(input_list=input_file_list)
    # print(start_end_intervals)

    # Sort Input List, withOut using sort function
    start_end_intervals_sorted = cust_heap_sort(input_list=start_end_intervals)
    # print(start_end_intervals_sorted)

    # Clean the Output file if present
    cleanup_output_file(output_file=output_file_name)

    # Find minimum checkout counters required
    min_counter_req = min_counters(intervals=start_end_intervals_sorted)
    # print(min_counter_req)

    # Write the minimum checkout counters required as a file
    write_output(output_file=output_file_name, to_write=min_counter_req)

    print(f"Program Successfully executed!")
