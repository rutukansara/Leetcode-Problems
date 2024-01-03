class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = {}
        for num in arr:
            counter[num] = counter.get(num, 0) + 1
        counter_set = set(counter.values())
        return len(counter_set) == len(counter)