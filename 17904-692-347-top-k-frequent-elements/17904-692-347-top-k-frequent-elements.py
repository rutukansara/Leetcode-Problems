class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        top_k = [key for key, value in sorted(hashmap.items(), key=lambda x: x[1], reverse=True)[:k]]
        return top_k