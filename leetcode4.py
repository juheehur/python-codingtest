# Generated from blog post
# Title: Leetcode-4
# Date: 2025-02-15
# Code Block 1
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2

        merged.sort()
        n = len(merged)

        median = merged[n//2] if n%2 !=0 else (merged[n//2-1]+merged[n//2])/2

        return median