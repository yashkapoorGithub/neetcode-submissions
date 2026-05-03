class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxCount = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                maxCount = max(count, maxCount)
                count = 0
                i += 1
                continue
            count += 1
            i += 1
        maxCount = max(count, maxCount)
        return maxCount