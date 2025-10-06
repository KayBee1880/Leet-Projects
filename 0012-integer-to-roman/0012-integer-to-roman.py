#I will go ahead and make two efficient solutions for this problem 
class Solution:
    def intToRoman(self, num: int) -> str:
        #Solution 1

    
    #Solution 2 : Using a hashmap with ordered arrangement starting in reverse
        res = ""
        symList = {"M":1000,"CM":900,"D":500,"CD":400,"C":100,"XC":90,"L":50,"XL":40,"X":10,"IX":9,"V":5,"IV":4,"I":1}
        for sym, val in symList.items():
            while num >= val:
                res += sym
                num -= val
        return res
    

    
        