class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # if target in in nums list
        if target in nums:
            # return the index of target in nums
            return nums.index(target)
        # if target is not in the nums list
        else:
            # insert the number in the list
            nums.insert(0, target)
            # sort list
            nums.sort()
            return nums.index(target)

# OR

# using pointer method
# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         left, right = 0, len(nums)-1

#         while left <= right:
#             if target == nums[left]:
#                 return left
#             elif target == nums[right]:
#                 return right
#             elif nums[left] > target:
#                 return left
#             elif target > nums[right]:
#                 return right + 1
#             else:
#                 left += 1
#                 right -= 1
#         return left