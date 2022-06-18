import heapq


class Solution2:
    def minMeetingRooms(self, intervals):
        meeting_num = len(intervals)
        rooms = 0

        start = [0] * meeting_num
        end = [0] * meeting_num
        for index in range(meeting_num):
            start[index] = intervals[index][0]
            end[index] = intervals[index][1]

        # start.sort()
        # end.sort()
        end_i = 0
        for index in range(meeting_num):
            if start[index] < end[end_i]:
                rooms += 1
            else:
                end_i += 1
        return rooms


def main():
    # meetings = [[0, 4], [1, 7], [7, 10], [9, 11], [3, 8], [4, 2]]
    meetings = [[0, 2], [4, 4], [2, 4], [4, 2], [7, 3], [2, 6]]
    # meetings.sort()
    s = Solution2()
    print(s.minMeetingRooms(meetings))


if __name__ == '__main__':
    # meetings = [[2, 15], [36, 45], [9, 29], [16, 23], [4, 9]]

    # s = Solution2()
    # print(s.minMeetingRooms(meetings))
    main()


