class RandomizedSet:

    def __init__(self): 
        self.arr = []
        self.hashmap = {}

    def insert(self, val: int) -> bool:
        if val in self.hashmap: return False 
        self.arr.append(val)
        self.hashmap[val] = len(self.arr) - 1
        return True 
        
    def remove(self, val: int) -> bool:
        if val not in self.hashmap: return False 
        idx = self.hashmap[val]
        last_val = self.arr[-1]
        self.arr[idx] = last_val
        self.hashmap[last_val] = idx
        self.arr.pop()
        del self.hashmap[val]
        return True 

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()