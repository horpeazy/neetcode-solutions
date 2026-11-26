class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [0, 0, 0]

        for num in nums:
            colors[num] += 1

        pointer = 0
        for i in range(len(colors)):
            color_cnt = colors[i]
            while color_cnt > 0:
                nums[pointer] = i
                pointer += 1
                color_cnt -= 1
        



        