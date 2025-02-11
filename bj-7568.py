# Generated from blog post
# Title: [백준] 7568.덩치
# Date: 2025-02-11
# Code Block 1
def calculate_rank(N, people):
  ranks=[]

  for i in range (N):
    count=0
    for j in range(N):
      if people[i][0]<people[j][0] and people[j][1]<people[j][1]:
        count+=1
    ranks.append(count+1)
  return ranks


N = int(input())
people = [tuple(map(int, input().split())) for _ in range(N)]
rank = calculate_rank(N, people)

print(" ".join(map(str, rank)))