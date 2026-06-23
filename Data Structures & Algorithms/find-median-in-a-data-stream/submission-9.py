class MedianFinder:

    def __init__(self):
        self.storage = []
        heapq.heapify(self.storage)        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.storage,num)
        return

    def findMedian(self) -> float:
        new_heap = self.storage.copy()

        if len(new_heap) % 2 == 0:
            for i in range((len(new_heap) // 2) - 1):
                heapq.heappop(new_heap)
            n1 = heapq.heappop(new_heap)
            n2 = heapq.heappop(new_heap)
            return (n1 + n2) / 2
        else:
            for i in range(len(new_heap) // 2):
                heapq.heappop(new_heap)
            
            n1 = heapq.heappop(new_heap)
            return n1
