class Solution:
    def hammingWeight(self, n: int) -> int:
        hashmap = {}
        n = bin(n)[2:]
        for number in n:
            hashmap[number] = hashmap.get(number, 0) + 1
        if '1' in hashmap:
            return hashmap['1']
        return 0