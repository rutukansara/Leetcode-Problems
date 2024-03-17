class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        left, right = 0, n
        answer = []

        while left <= n-1:
            answer.append(nums[left])
            answer.append(nums[right])
            left += 1
            right += 1

        return answer
