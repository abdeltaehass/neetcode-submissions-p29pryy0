class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            bits = (n >> i) & 1
            res = res | (bits << (31 - i))
        return res