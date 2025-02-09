# Generated from blog post
# Title: [백준] 11653. 소인수분해 
# Date: 2025-02-09
# Code Block 1
n = int(input())

if n > 1:
    # 2로 먼저 나누어 떨어지는 만큼 나누기
    while n % 2 == 0:
        print(2)
        n //= 2

    # 3부터 √N까지 홀수만 체크
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            print(factor)
            n //= factor
        factor += 2 

    if n > 1:
        print(n)