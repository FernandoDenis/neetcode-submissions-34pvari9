class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # ["X","X","Y","Y"]
        # 
        # 1,1,x,1,1
        # 

        counter_of_task = Counter(tasks)

        maxHeap = []

        for freq in counter_of_task.values():
            maxHeap.append(-freq)

        heapq.heapify(maxHeap)

        q = deque()
        cycle = 0
        # (A,8)
        while maxHeap or q:
            cycle += 1

            if not maxHeap:
                cycle = q[0][1]
            else:
                freq = heapq.heappop(maxHeap) + 1

                if freq:
                    q.append((freq, cycle + n))

            if q and q[0][1] <= cycle:
                freq, time = q.popleft()

                heapq.heappush(maxHeap, freq)

        return cycle


        