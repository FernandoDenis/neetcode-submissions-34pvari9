class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #        
        # [1,2,3,4,5]
        # [3,4,5,1,2]
        # -2-2-2 3 -3  
        # 
        # [5,8,2,8]
        # [6,5,6,6]
        # -1 3 -42

        index = []

        for i in range(len(gas)):
            difference = gas[i] - cost[i - 1]
            index.append(gas[i] - cost[i])
            gas[i] = difference
            
        
        addition = sum(gas)

        if addition < 0:
            return -1

        idx = 0
        add = 0
        if addition >= 0:
            for i in range(len(index)):
                if index[idx] < index[i] and index[(i + 1) - len(index)] + index[i] >= add:
                    idx = i
                    add = index[(i + 1) - len(index)] + index[i]
            return idx

            

        