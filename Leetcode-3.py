# Generated from blog post
# Title: [Leetcode] 3. Longest Substring Without Repeating Characters
# Date: 2025-02-06
# Code Block 1
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        char_set = set()
        left =0
        max_length =0

        for right in range (len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length