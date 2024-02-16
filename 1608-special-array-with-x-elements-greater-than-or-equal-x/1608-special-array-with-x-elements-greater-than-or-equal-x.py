class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for x in range(0, 1001):
            count = 0
            for y in nums:
                if y >= x:
                    count += 1
            if count == x:
                return x
        return -1