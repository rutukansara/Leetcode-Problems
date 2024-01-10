class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        function = 0
        answer = []
        for i in range(len(nums)):
            function = (a*(nums[i]**2)) + (b*nums[i]) + c
            answer.append(function)
        answer.sort()
        return answer