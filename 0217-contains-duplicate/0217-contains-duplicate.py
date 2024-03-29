class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}

        for i in range(len(nums)):
            hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1
            
        for k, v in hashmap.items():
            if v >= 2:
                return True