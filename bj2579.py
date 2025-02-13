# Generated from blog post
# Title: bj-2579
# Date: 2025-02-13
# Code Block 1
# 계단의 개수를 입력받습니다.
n= int(input())

# 각 계단에 쓰여진 점수를 저장할 리스트를 생성합니다.
# 인덱스를 1부터 사용하기 위해 크기를 (n+1)로 설정하고, 기본값은 0으로 초기화합니다.
score = [0]*(n+1)

# 1번 계단부터 n번 계단까지 각 계단의 점수를 입력받아 score 리스트에 저장합니다.
for i in range (1,n+1):
    score[i] = int(input())

# dp[i]는 i번째 계단까지 올라왔을 때 얻을 수 있는 최대 점수를 저장할 리스트입니다.
dp = [0]*(n+1)

# 초기 조건 설정:
# 계단이 하나일 경우, 최대 점수는 첫 번째 계단의 점수입니다.
if n>=1:
    dp[1] = score[1]

# 계단이 두 개일 경우, 반드시 1번과 2번 계단을 연속해서 밟아야 하므로 점수의 합이 최대 점수가 됩니다.
if n>=2:
    dp[2] = score[1]+score[2]

# 3번 계단부터 n번 계단까지 dp 배열을 채워나갑니다.

for i in range (3,n+1):
    dp[i] = max(dp[i-2] + score[i], dp[i-3] + score[i-1] + score[i])

print(dp[n])