class Solution:
    def search(self, nums: List[int], target: int) -> int:
    # simply traversing through the list
        if target in nums:
            return (nums.index(target))
        return -1