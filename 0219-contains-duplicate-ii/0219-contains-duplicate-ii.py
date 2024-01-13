class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        chars = {}
        for i, num in enumerate(nums):
            if num in chars and abs(i-chars[num])<=k:
                return True
            chars[num] = i
        
        return False