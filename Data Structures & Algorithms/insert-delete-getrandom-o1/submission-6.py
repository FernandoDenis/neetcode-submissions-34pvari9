class RandomizedSet:
    # ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
    # [[],               [1],        [2],        [2],        [],       [1],         [2],   []]
    # dictPos {2:1}
    # random [2]
    # output null, true, false, true, 2, true, false, 2
    def __init__(self):
        self.dictPos = {}
        self.random = []

    def insert(self, val: int) -> bool:
        if val in self.dictPos:
            return False
        else:
            self.dictPos[val] = len(self.random)
            self.random.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val not in self.dictPos:
            return False
        else:
            position = self.dictPos[val]

            self.dictPos[self.random[-1]] = position 

            self.random[position], self.random[-1] = self.random[-1], self.random[position]
            self.random.pop()

            del self.dictPos[val]
            return True

    def getRandom(self) -> int:
        random_number = random.choice(self.random)
        return random_number


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()