import random
class RandomizedSet:
    def __init__(self):
        self.numslist = []
        self.numsMap = {}
    def insert(self,val):
        if val in self.numsMap: return False
        self.numslist.append(val)
        self.numsMap[val] = len(self.numslist) - 1
        return True

    def remove(self,val):
        if val not in self.numsMap: return False
        idx = self.numsMap[val]
        last_el = self.numslist[-1]
        self.numslist[idx] = last_el
        self.numsMap[last_el] = idx
        self.numslist.pop()
        del self.numsMap[val]
        return True
    def getRandom(self):
        return random.choice(self.numslist)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()