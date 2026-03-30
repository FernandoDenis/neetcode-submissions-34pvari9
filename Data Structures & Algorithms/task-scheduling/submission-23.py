class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # ["A","A","A","B","C"]
        #  
        # 
        # time 9
        counter_task = Counter(tasks)
        maxHeap = []
        for freq in counter_task.values():
            maxHeap.append(-freq)

        heapq.heapify(maxHeap)
        time = 0
        q = deque()

        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                freq = heapq.heappop(maxHeap) + 1
                if freq:
                    q.append((freq, time + n))

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time

        