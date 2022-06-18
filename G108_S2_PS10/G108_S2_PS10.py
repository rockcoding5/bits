import heapq
import os
import sys


def read_input_file(inputFile):
    try:
        with open(os.path.join(parentFolderPath, inputFile), 'r') as input_file:
            lines = input_file.readlines()
            if len(lines) == 0:
                print('Input file is Empty! Please check')
            else:
                input_list = []
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
        print(inputFile + ' Input file not found! Please check')
        exit()
    except:  # Handle any other error
        print(inputFile + ' Cannot Read input file! Please check')
        exit()


def cleanup_output_file(outputFile):
    if os.path.isfile(os.path.join(parentFolderPath, outputFile)):
        os.remove(os.path.join(parentFolderPath, outputFile))


def write_output(outputFile, to_write):
    """
    This function just writes the text given to it in the output file (output*.txt)
    :param to_write:
    :return: None
    """
    to_write = 'Minimum Checkout counters required: ' + str(to_write)
    print(to_write)
    with open(outputFile, 'a+') as outf:
        outf.write(to_write)


def shift_up_with_parent(heap, pos):
    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]
    # Bubble up the smaller child until hitting a leaf.
    childpos = 2 * pos + 1  # leftmost child position
    while childpos < endpos:
        # Set childpos to index of smaller child.
        rightpos = childpos + 1
        if rightpos < endpos and not heap[childpos] < heap[rightpos]:
            childpos = rightpos
        # Move the smaller child up.
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2 * pos + 1
    # The leaf at pos is empty now.  Put newitem there, and bubble it up
    # to its final resting place (by sifting its parents down).
    heap[pos] = newitem
    shift_down_with_child(heap, startpos, pos)


def shift_down_with_child(heap, startpos, pos):
    newitem = heap[pos]
    # Follow the path to the root, moving parents down until finding a place
    # newitem fits.
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if newitem < parent:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem


# Push item onto heap, maintaining the heap invariant.
def heappush(heap, item):
    heap.append(item)
    shift_down_with_child(heap, 0, len(heap) - 1)


# Fast version of a heappush followed by a heappop.
def heappushpop(heap, item):
    if heap and heap[0] < item:
        item, heap[0] = heap[0], item
        shift_up_with_parent(heap, 0)
    return item


def min_meeting_rooms(intervals):
    # meetings = [[0, 5], [1, 7], [7, 10], [9, 11], [3, 8], [6, 2]]
    intervals.sort()
    # meetings = [[0, 5], [1, 7], [3, 8], [6, 2], [7, 10], [9, 11] ]
    rooms = 0
    meeting = []
    for interval in intervals:
        if not meeting:
            meeting.append(interval[1])
            rooms += 1
        else:
            if interval[0] >= meeting[0]:
                # heapq.heappushpop(meeting, interval[1])  # pop the first heap element
                heappushpop(meeting, interval[1])  # pop the first heap element
            else:
                # heapq.heappush(meeting, interval[1])
                heappush(meeting, interval[1])
                rooms += 1
    return rooms


def min_counters(intervals):
    intervals.sort()
    counters = 0
    counter_list = []
    for interval in intervals:
        if not counter_list:
            counter_list.append(interval[1])
            counters += 1
        else:
            if interval[0] >= counter_list[0]:
                heappushpop(counter_list, interval[1])  # pop the first heap element
            else:
                heappush(counter_list, interval[1])
                counters += 1
    return counters


if __name__ == '__main__':
    # Initialize the Paths. Current folder is parent folder
    parentFolderPath = ''
    inputFileName = 'inputPS10.txt'
    outputFile = 'outputPS10.txt'

    # Read the Input file to create a Binary Tree
    input_file_list = read_input_file(inputFile=inputFileName)
    print('Input File List : ' + str(input_file_list))

    # Clean the Output file if present
    cleanup_output_file(outputFile=outputFile)

    # Find minimum meeting rooms required
    print(min_meeting_rooms(input_file_list))

    # Find minimum counters required
    min_counter_req = min_counters(input_file_list)
    print(min_counter_req)

    write_output(outputFile, min_counter_req)

    print(f"Program Successfully executed!")
