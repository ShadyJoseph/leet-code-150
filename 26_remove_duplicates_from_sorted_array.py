class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for num in nums:
            if k == 0 or num != nums[k-1]:
                nums[k] = nums
                k = k+1
        return k
