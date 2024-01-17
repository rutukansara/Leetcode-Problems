class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        print(counter)

        answer = next((k for k, v in counter.items() if v == 1), None)
        return answer