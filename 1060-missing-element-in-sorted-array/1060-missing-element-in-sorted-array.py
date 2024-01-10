from typing import List

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        pointer = 0
        for i in range(len(nums) - 1):
            diff = nums[i + 1] - nums[i] - 1
            if pointer + diff >= k:
                return nums[i] + k - pointer
            else:
                pointer += diff
        return nums[-1] + k - pointer
