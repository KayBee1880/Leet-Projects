class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        p = nums
        prefix = [0] * (n+1)
        for i in range(n): 
            prefix[i+1] = prefix[i] + nums[i]
        dq = deque()
        best = float("inf")
        for j in range(n+1): 
            while dq and prefix[j] - prefix[dq[0]] >= k: 
                best = min(best, j - dq[0])
                dq.popleft()
            while dq and prefix[j] < prefix[dq[-1]]: 
                dq.pop()
            dq.append(j)

        return best if best != float("inf") else -1