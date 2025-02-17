# Generated from blog post
# Title: Leetcode-3
# Date: 2025-02-17
# Code Block 1
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1  # 중복이 없을 때까지 왼쪽 포인터 이동

            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)  # 최댓값 갱신

        return max_length