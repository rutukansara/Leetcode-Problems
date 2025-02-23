# no duplicate triplets allowed
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for idx, num in enumerate(nums):
            if idx > 0 and num == nums[idx-1]:
                continue
            
            left, right = idx + 1, len(nums)-1
            while left < right:
                threeSum = num + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    res.append([num, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return res