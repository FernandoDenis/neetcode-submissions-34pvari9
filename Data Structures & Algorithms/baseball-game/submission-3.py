class Solution:
    def calPoints(self, operations: List[str]) -> int:
        #             i                                        
        # ["10","20",40,"C","+"]
        total = 0

        for i in range(len(operations)):
            if operations[i] == "+":
                add = int(operations[i - 1]) + int(operations[i - 2])
                total += add
                operations[i] = add
            elif operations[i] == "C":
                total -= int(operations[i - 1])
                operations[i] = operations[i - 2]
                operations[i - 1] = operations[i - 3]
            elif operations[i] == "D":
                mult = int(operations[i - 1]) * 2
                total += mult
                operations[i] = mult
            else:
                total += int(operations[i])
                operations[i] = int(operations[i])

        return total
