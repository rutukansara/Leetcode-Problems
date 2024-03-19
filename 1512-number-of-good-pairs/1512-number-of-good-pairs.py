class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashtable = {}
        for i in nums:
            hashtable[i] = hashtable.get(i, 0) + 1
        sum = 0
        for k, v in hashtable.items():
            if v > 1:
                sum = sum + (v*(v-1))/2
        return int(sum)