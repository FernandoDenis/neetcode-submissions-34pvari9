class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # stack [5,10]
        #   op 
        # ["5","D","+","C"]
        if not operations:
            return 0

        stack = []
        for op in operations:
            if op == "+":
                total = stack[-1] + stack[-2]
                stack.append(total)
            elif op == "C":
                stack.pop()
            elif op == "D":
                total = stack[-1] * 2
                stack.append(total)
            else:
                number = int(op)
                stack.append(number)

        return sum(stack)

        