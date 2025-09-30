class Solution:
    def  towerOfHanoi(self, n, fromm, to, aux):
        # code here
        if n == 0: return 0
        move1 = self.towerOfHanoi(n-1,fromm, aux, to)
        move2 = 1
        move3 = self.towerOfHanoi(n-1, aux, to, fromm)
        return move1 + move2 + move3