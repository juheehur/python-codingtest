# Generated from blog post
# Title: Leetcode-12
# Date: 2025-02-21
# Code Block 1
class Solution:
    def intToRoman(self, num: int) -> str:
        roman_numerals = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
            (1, "I")
        ]
        
        result = ""
        for value, symbol in roman_numerals:
            while num >= value:
                result += symbol
                num -= value
        return result