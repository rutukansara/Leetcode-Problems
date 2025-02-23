class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # hashmap = {}

        # for num in nums:
        #     hashmap[num] = hashmap.get(num, 0) + 1
        
        # for key, value in hashmap.items():
        #     if value > 1:
        #         return True
        # return False
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False