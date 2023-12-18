class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # hashmap
        count = {}
        answer, cnt = 0, 0

        for n in nums:
            count[n] = 1 + count.get(n, 0)
            if count[n] > cnt:
                answer = n
            else:
                answer = answer
            cnt = max(count[n], cnt)
        return answer

        
        # this code exceeds the time limit
        # n = len(nums)
        # majority = math.floor(n/2)
        # for i in nums:
        #     if nums.count(i) > majority:
        #         return i