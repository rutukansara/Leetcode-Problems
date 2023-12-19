class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = [1] * len(nums)
        for i in range(len(nums)):
            squares[i] = nums[i] **2
        squares.sort()
        return squares