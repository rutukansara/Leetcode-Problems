class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        array = set(nums)
        res = []

        for i in range(1, len(nums)+1):
            if i not in array:
                res.append(i)
        return res