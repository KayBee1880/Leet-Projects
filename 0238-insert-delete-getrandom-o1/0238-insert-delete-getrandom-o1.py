from random import choice
class RandomizedSet:

    def __init__(self):
        self.cache = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.cache: 
            return False
        self.nums.append(val)
        self.cache[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.cache: 
            return False 
        indx = self.cache[val]
        last_val = self.nums[-1]
        self.nums[indx] = last_val
        self.cache[last_val] = indx
        self.nums.pop()
        del self.cache[val]
        return True

    def getRandom(self) -> int:
        return choice(self.nums)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna