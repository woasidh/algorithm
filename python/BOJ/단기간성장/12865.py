# 냅색 알고리즘...
# 풀이 봄...

import sys

# input 처리
n, k = map(int, sys.stdin.readline().split());
bags = [];
for _ in range(n):
    weight, value = map(int, sys.stdin.readline().split());
    bags.append([weight, value]);
answer = -1;

dp = [[-1 for i in range(k + 1)] for j in range(n)];

for i in range(k + 1):
    if i < bags[0][0]: dp[0][i] = 0;
    else: dp[0][i] = bags[0][1];

for i in range(1, n):
    weight, value = bags[i];
    for j in range(k + 1):
        # 않 넣었을 때
        noPush = dp[i - 1][j];

        # 넣었을 때
        push = value + dp[i - 1][j - weight] if j >= weight else 0;

        dp[i][j] = max(noPush, push);

print(dp[n - 1][k]);
