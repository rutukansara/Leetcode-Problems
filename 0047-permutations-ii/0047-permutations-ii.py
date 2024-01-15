class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]
        arr = []
        for i in range(len(nums)):
            current = nums[i]
            remaining = nums[:i] + nums[i+1:]

            for p in self.permuteUnique(remaining):
                if [current] + p not in arr:
                    arr.append([current] + p)

        return arr