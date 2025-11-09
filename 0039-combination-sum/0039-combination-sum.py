class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(start, path, remaining):
            if remaining == 0:
                res.append(path[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    continue 
                path.append(candidates[i])
                backtrack(i, path, remaining - candidates[i])
                path.pop()
        backtrack(0,[],target)
        return res
        
    ##Time and space complexity 
    ##Space: The depth of the recursion tree is O(target / min(candidates)) in the worst case
    ##Time: O(n target/s )Since s is a constant depending on the input values, the worst-case complexity is O(n^m), where m = target / min(candidates).