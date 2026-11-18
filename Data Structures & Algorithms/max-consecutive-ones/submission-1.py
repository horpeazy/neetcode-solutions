class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxCount = 0
        for i in range(len(nums)):
            count = count + 1 if nums[i] else 0
            maxCount = max(maxCount, count)

        return maxCount

        