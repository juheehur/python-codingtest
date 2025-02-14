# Generated from blog post
# Title: leetcode-7
# Date: 2025-02-14
# Code Block 1
class Solution:
    def reverse(self, x: int) -> int:
        if x > 2**31 - 1 or x < -2**31:
            return 0

        else:
            reverse = 0
            num = abs(x) 
            while num > 0:
                n = num % 10
                reverse = reverse * 10 + n
                num //= 10
            
            if reverse > 2**31 - 1 or reverse < -2**31:
                return 0
            
            return reverse if x > 0 else -reverse