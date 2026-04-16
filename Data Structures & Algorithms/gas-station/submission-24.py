class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # [1,2,3,4]
        # [2,2,4,1]
        # -1-1-1 3 

        if sum(gas) < sum(cost):
            return -1

        total = 0
        position = 0 
        for i in range(len(gas)):
            total += (gas[i] - cost[i])
            
            if total < 0:
                position = i + 1
                total = 0

        return position
        