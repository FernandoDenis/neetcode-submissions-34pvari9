class RandomizedSet:
    # [3,2]
    # 2:1, 3:0

    def __init__(self):
        self.numbers = dict()
        self.storage = []

    def insert(self, val: int) -> bool:
        if val in self.numbers:
            return False
        else:
            self.storage.append(val)
            self.numbers[val] = len(self.storage) - 1
            return True

    def remove(self, val: int) -> bool:
        if val in self.numbers:
            # deleting in array
            pos = self.numbers[val]
            if pos != len(self.storage) - 1:
                self.storage[pos] = self.storage[-1]
                self.storage.pop() 
                self.numbers[self.storage[pos]] = pos
            else:
                self.storage.pop()

            del self.numbers[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.storage)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()