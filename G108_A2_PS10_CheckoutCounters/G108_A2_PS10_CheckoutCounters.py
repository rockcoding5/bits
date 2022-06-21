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
        with open(os.path.join(parentFolderPath, input_file), 'r') as input_file:
            lines = input_file.readlines()
            if len(lines) == 0:
                print('Input file is Empty! Please check')
            else:
                input_list = []
                input_list2 = []
                try:
                    for line in lines:
                        input_list.append([int(sub_line) for sub_line in
                                           line.rstrip('\n').strip("''[]'").replace(' ', '').split(',')])
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
    if os.path.isfile(os.path.join(parentFolderPath, output_file)):
        os.remove(os.path.join(parentFolderPath, output_file))


def write_output(output_file, to_write):
    """
    This function just writes the text given to it in the output file (output*.txt)
    :param output_file:
    :param to_write:
    :return: None
    """
    to_write = 'Minimum Checkout counters required: ' + str(to_write)
    print(to_write)
    with open(output_file, 'a+') as outf:
        outf.write(to_write)


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
    This function to Fast version of a heappush followed by a heappop.
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
    # Sort the input List dataset - [start point, checkout time]
    intervals.sort()
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
    parentFolderPath = ''
    input_file_name = 'inputPS10.txt'
    output_file_name = 'outputPS10.txt'

    # Read the Input file and create a List with list of Integer entries [start point, checkout time]
    input_file_list = read_input_file(input_file=input_file_name)
    # print('Input File List : ' + str(input_file_list))

    # Calculate the End time by using start time and required checkout time
    start_end_intervals = get_end_time(input_list=input_file_list)
    # print(start_end_intervals)

    # Clean the Output file if present
    cleanup_output_file(output_file=output_file_name)

    # Find minimum checkout counters required
    min_counter_req = min_counters(intervals=start_end_intervals)
    # print(min_counter_req)

    # Write the minimum checkout counters required as a file
    write_output(output_file=output_file_name, to_write=min_counter_req)

    print(f"Program Successfully executed!")
