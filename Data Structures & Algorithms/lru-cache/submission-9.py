class LRUCache:

    #[2:20, 3:30]
    # null, null, 10, null, 20, -1

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
            return

        if len(self.cache) + 1 > self.capacity:
            self.cache.popitem(last = False)
        self.cache[key] = value

        return
        
        
        
