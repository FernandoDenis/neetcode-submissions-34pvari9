class MyStack:
    # 1,2,3
    # R True
    # [3]
    # [1]

    # [1]

    def __init__(self):
        self.storage = deque()
        self.queue = deque()
        self.reverse = False

    def push(self, x: int) -> None:
        self.storage.append(x)
        return

    def pop(self) -> int:
        if not self.storage and not self.queue:
            return
        elif not self.queue:
            self.reverse = False
            while self.storage:
                self.queue.append(self.storage.popleft())
            
            self.queue.reverse()
            self.reverse = True
            return self.queue.popleft()
        if self.reverse:
            return self.queue.popleft()
        else:
            self.queue.reverse()
            self.reverse = True
            return self.queue.popleft()

    def top(self) -> int:
        if not self.storage and not self.queue:
            return
        elif self.storage:
            return self.storage[-1]
        if self.reverse:
            return self.queue[0]
        else:
            return self.queue[-1]

    def empty(self) -> bool:
        if not self.storage and not self.queue:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()