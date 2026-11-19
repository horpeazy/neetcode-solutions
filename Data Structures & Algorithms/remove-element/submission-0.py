class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        valPointer = 0;
        for i in range(len(nums)):
            if nums[i] != val:
                nums[valPointer] = nums[i]
                valPointer += 1

        return valPointer
