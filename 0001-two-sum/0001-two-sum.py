class Solution:
    def twoSum(self, nums: List[int], target: int):
        # use a hashmap to store nums and their indices
        hashmap = {}

        for idx, num in enumerate(nums):
            difference = target - num
            if difference in hashmap:
                return [idx, hashmap[difference]]
            hashmap[num] = idx