# Generated from blog post
# Title: [Leetcode] 9. Palindrome Number
# Date: 2025-02-07
# Code Block 1
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)==str(x)[::-1]