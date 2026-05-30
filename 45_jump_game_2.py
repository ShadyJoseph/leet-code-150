"""
Brute Force (Recursive DFS)
complexity O(2^n)


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        def dfs(i):
            if i >= n - 1:
                return 0
            min_jumps = float("inf")
            for jump in range(1, nums[i] + 1):
                min_jumps = min(min_jumps, 1 + dfs(jump + i))

            return min_jumps

        return dfs(0)

"""

"""
The DP way Top down and memo the answers to be reused and save computations
complexity O(2^n) but better than brute force
class Solution:
    def jump(self, nums):
        n = len(nums)
        memo = {}

        def dfs(i):
            if i >= n - 1:
                return 0

            if i in memo:
                return memo[i]

            ans = float('inf')

            for jump in range(1, nums[i] + 1):
                ans = min(ans, 1 + dfs(i + jump))

            memo[i] = ans
            return ans

        return dfs(0)

"""
"""
The greedy solution BFS
complexity o(n)
"""


class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = left = right = 0
        while right < len(nums) - 1:
            farthest = 0
            for i in range(left, right + 1):
                farthest = max(farthest, nums[i] + i)
            left = right + 1
            right = farthest

            jumps += 1
        return jumps
