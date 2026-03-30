class RandomizedSet:

    def __init__(self):
        self.random = dict()

    def insert(self, val: int) -> bool:
        if val not in self.random:
            self.random[val] = 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val not in self.random:
            return False
        else:
            del self.random[val]
            return True

    def getRandom(self) -> int:
        for key in self.random:
            return key 


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()