class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.history = deque()
        self.cache = dict()

    def get(self, key: int) -> int:
        print(self.history)
        print(self.cache)
        if key in self.cache:
            value, idx = self.cache[key]
            self.history[idx] = -1
            self.history.append(key)

            self.cache[key][1] = len(self.history) - 1
            
            return value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key][0] = value
            idx = self.cache[key][1]
            self.history[idx] = -1
            self.history.append(key)

            self.cache[key][1] = len(self.history) - 1
            
            return 
        
        if len(self.cache) + 1 <= self.capacity:
            self.cache[key] = [value, len(self.history)]
            self.history.append(key)
            return 
        else:
            for idx, key1 in enumerate(self.history):
                if key1 != -1:
                    least_recently_used_key = key1
                    self.history[idx] = -1
                    break

            del self.cache[least_recently_used_key]

            self.cache[key] = [value, len(self.history)]
            self.history.append(key)

            return 