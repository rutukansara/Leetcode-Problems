class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningsum = []

        for i in range(len(nums)):
            currentsum = 0
            for j in nums[:i+1]:
                currentsum += j

            runningsum.append(currentsum)
        return runningsum