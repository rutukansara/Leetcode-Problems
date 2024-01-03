class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        key = next((key for key, value in counter.items() if value == 1), None)
        return key