# Generated from blog post
# Title: Leetcode-5
# Date: 2025-02-19
# Code Block 1
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_from_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        longest = ""

        for i in range(len(s)):
            # Odd-length palindrome (centered at i)
            odd_palindrome = expand_from_center(i, i)
            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome
            
            # Even-length palindrome (centered between i and i+1)
            even_palindrome = expand_from_center(i, i + 1)
            if len(even_palindrome) > len(longest):
                longest = even_palindrome

        return longest