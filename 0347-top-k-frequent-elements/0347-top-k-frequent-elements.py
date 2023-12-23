class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_int = {}
        top_k = []

        for n in nums:
            map_int[n] = map_int.get(n, 0) + 1

        sorted_keys = sorted(map_int.items(), key = lambda x: x[1], reverse = True)
        
        for key, val in sorted_keys[:k]:
            top_k.append(key)

        return top_k