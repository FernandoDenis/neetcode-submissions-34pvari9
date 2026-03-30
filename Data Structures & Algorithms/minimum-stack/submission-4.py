class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.minStack.append(val)
        else:
            self.stack.append(val)
            if self.minStack[-1] >= val:
                self.minStack.append(val)
        return 

    def pop(self) -> None:
        if self.stack:
            element = self.stack.pop()

            if element == self.minStack[-1]:
                self.minStack.pop()
        return 

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return         

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]
        return
        
