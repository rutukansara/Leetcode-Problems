class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        nums = 0
        for s in stones:
            if s in jewels:
                nums+=1
        return nums