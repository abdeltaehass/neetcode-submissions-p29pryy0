class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i + 1] and dp[i + 2]
        one_back = 1
        two_back = 1

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                current = 0
            else:
                current = one_back

                # Check whether the next two digits form 10 through 26
                if (
                    i + 1 < len(s)
                    and 10 <= int(s[i:i + 2]) <= 26
                ):
                    current += two_back

            two_back = one_back
            one_back = current

        return one_back