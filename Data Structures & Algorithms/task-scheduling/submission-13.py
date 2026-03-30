class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # ["A","A","A","B","C"]
        # A:3, B:1, C:1
        # 
        # 1

        counter_letters  = Counter(tasks)
        maxHeap = []
        for key, value in counter_letters.items():
            maxHeap.append((-value, key, 0))

        heapq.heapify(maxHeap)
        cycle = 0 # 5

        # [,]

        while maxHeap:
            print(maxHeap)

            freq, letter, lastCycle = heapq.heappop(maxHeap) # [(-1, 'A', 1), (-1, 'B', 2), (-1, 'C', 0), (-1, 'D', 0)]

            cycle += 1 # 4
            next_use = cycle + n + 1 # 5
            array_task = [] # []
            while maxHeap and cycle < next_use - 1: # 3 4
                cycle += 1

                freq1, letter1, lastCycle1 = heapq.heappop(maxHeap) # 
                array_task.append((freq1 + 1, letter1, cycle))

            for tup in array_task:
                if tup[0] == 0:
                    continue
                heapq.heappush(maxHeap, tup)
            # 
            if cycle == next_use:
                if freq + 1 < 0:
                    heapq.heappush(maxHeap, (freq + 1, letter, cycle))
            else:
                if freq + 1 == 0:
                    continue
                heapq.heappush(maxHeap, (freq + 1, letter, lastCycle + 1)) 
                cycle = next_use - 1 # 8

        
        return cycle
                



