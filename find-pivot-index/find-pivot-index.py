class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            sumleft = sum(nums[:i])
            sumright = sum(nums[i+1:])
        
            if sumleft == sumright:
                return i
        return -1