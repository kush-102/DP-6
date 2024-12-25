class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.start = 0
        self.end = 0
        for i in range(len(s)):
            # Expand around the center for odd-length palindromes
            self.expand_around(s, i, i)
            # Expand around the center for even-length palindromes
            self.expand_around(s, i, i + 1)

        # Return the longest palindrome
        return s[self.start : self.end + 1]

    def expand_around(self, s: str, left: int, right: int):
        # Expand outward while the characters match
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        # Update the start and end if the current palindrome is longer
        left += 1
        right -= 1
        if right - left > self.end - self.start:
            self.start = left
            self.end = right
        # time complexity is O(n^2)
        # space complexity is O(1)
        # dynamic programming Solution
        start = 0
        end = 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1):
                if s[i] == s[j]:
                    if i - j <= 1 or dp[i - 1][j + 1]:
                        dp[i][j] = True
                        if i - j > end - start:
                            start = j
                            end = i
                    else:
                        dp[i][j] = False
                else:
                    dp[i][j] = False
        return s[start : end + 1]

    # time complexity is O(n^2)
    # space complexity is O(n^2)
