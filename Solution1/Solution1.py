import heapq

class Solution1:
    def minMeetingRooms(self, intervals):
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
                    heapq.heappushpop(meeting, interval[1])  # pop the first heap element
                else:
                    heapq.heappush(meeting, interval[1])
                    rooms += 1
        return rooms


def main():
    # meetings = [[0, 4], [1, 7], [7, 10], [9, 11], [3, 8], [4, 2]]
    meetings = [[0, 2], [4, 4], [2, 4], [4, 2], [7, 3], [2, 6]]
    s = Solution1()
    print(s.minMeetingRooms(meetings))


if __name__ == '__main__':
    # meetings = [[2, 15], [36, 45], [9, 29], [16, 23], [4, 9]]

    # s = Solution2()
    # print(s.minMeetingRooms(meetings))
    main()


