class RandomizedSet:
    
    def __init__(self):
        self.hashSet = {} # 2:0
        self.array = [] # [2]

    def insert(self, val: int) -> bool:
        if val in self.hashSet:
            return False
        
        self.hashSet[val] = len(self.array)
        self.array.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.hashSet:
            return False

        pos = self.hashSet[val]
        self.array[pos],self.array[-1] = self.array[-1], self.array[pos]
        self.hashSet[self.array[pos]] = pos
        # delete
        del self.hashSet[val]
        self.array.pop()

        return True

    def getRandom(self) -> int:
        return random.choice(self.array)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()