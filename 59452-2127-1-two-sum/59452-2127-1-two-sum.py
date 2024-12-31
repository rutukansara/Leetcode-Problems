# exactly one solution
# cant use the same element twice
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for idx, num in enumerate(nums):
            difference = target - num
            if difference in hashmap:
                return [idx, hashmap[difference]]
            hashmap[num] = idx