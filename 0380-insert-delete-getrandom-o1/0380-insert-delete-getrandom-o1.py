from random import choice
class RandomizedSet:

    def __init__(self):
        self.cache = set()

    def insert(self, val: int) -> bool:
        if val in self.cache: 
            return False
        self.cache.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.cache: 
            return False 
        self.cache.discard(val)
        return True

    def getRandom(self) -> int:
        return choice(list(self.cache))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna