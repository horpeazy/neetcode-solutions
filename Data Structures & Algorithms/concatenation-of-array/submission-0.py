class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        newArr = [0] * 2 * n
        for i in range(len(nums)):
            newArr[i] = newArr[i + n] = nums[i]

        return newArr
        