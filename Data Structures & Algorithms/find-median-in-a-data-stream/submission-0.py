class MedianFinder:

    def __init__(self):
        self.minHeap = []
        heapq.heapify(self.minHeap)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.minHeap,(num, len(self.minHeap)))
        return 

    def findMedian(self) -> float:
        if self.minHeap:
            deleted_number = []
            length = len(self.minHeap)
            
            for i in range((length // 2) + 1):
                if self.minHeap:
                    deleted_number.append(heapq.heappop(self.minHeap))
                else:
                    break

            if length % 2 == 0:
                median = (deleted_number[-1][0] + deleted_number[-2][0]) / 2
            else:
                median = deleted_number[-1][0]

            while deleted_number:
                heapq.heappush(self.minHeap, deleted_number.pop())

            return median

        