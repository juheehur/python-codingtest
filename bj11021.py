# Generated from blog post
# Title: bj-11021
# Date: 2025-02-18
# Code Block 1
T = int(input())

for i in range(1, T + 1):
    a, b = map(int, input().split())
    print(f"Case #{i}: {a + b}")