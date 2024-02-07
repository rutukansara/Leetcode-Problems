class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)

        int_sum = a + b
        bin_sum = bin(int_sum)[2:]

        return bin_sum