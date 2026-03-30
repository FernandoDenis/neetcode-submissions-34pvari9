class MinStack:

    def __init__(self):
        self.stack = []
        self.minHeap = []
        heapq.heapify(self.minHeap)

    def push(self, val: int) -> None:
        self.stack.append(val)
        heapq.heappush(self.minHeap, val)
        return 

    def pop(self) -> None:
        if self.stack:
            element = self.stack.pop()
            self.minHeap = self.stack.copy()
            heapq.heapify(self.minHeap)
        return 

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return

    def getMin(self) -> int:
        if self.stack:
            return self.minHeap[0]
        
