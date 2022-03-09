import sys

n = int(sys.stdin.readline());
steps = [-1];
for _ in range(n):
    steps.append(int(sys.stdin.readline()));

# [1, 1, 1, 1, 1, 1];
dp = [[-1, -1]];
dp.append([steps[1], 0]);
if n == 1: print(steps[1]);
else:
    dp.append([steps[2], steps[1] + steps[2]]);
    for i in range(3, n + 1):
        dp.append([max(dp[i - 2][0], dp[i - 2][1]) + steps[i], dp[i - 1][0] + steps[i]]);
    print(max(dp[n][0], dp[n][1]));