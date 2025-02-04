# Generated from blog post
# Title: [Leetcode] 1768. Merge Strings Alternately
# Date: 2025-02-04
# Code Block 1
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        merged = []
        i,j = 0,0
        while i < len(word1) or j< len(word2):
            if i<len(word1):
                merged.append(word1[i])
                i +=1
            if j<len(word2):
                merged.append(word2[j])
                j +=1
        return ' '.join(merged)