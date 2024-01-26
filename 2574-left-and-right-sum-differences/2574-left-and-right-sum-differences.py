class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftArray = []
        rightArray = []
        answer = []
        for i in range(len(nums)):
            leftSum = sum(nums[:i])
            leftArray.append(leftSum)

            rightSum = sum(nums[i+1:len(nums)])
            rightArray.append(rightSum)
        
        for j in range(len(leftArray)):
            difference = abs(leftArray[j]-rightArray[j])
            answer.append(difference)
        return answer