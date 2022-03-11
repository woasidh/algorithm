import sys
import math

n = int(sys.stdin.readline());

if n == 3: print(1);
elif n == 4: print(-1);
else:
    dp = [math.inf for _ in range(n + 1)];
    dp[3], dp[5] = 1, 1;

    for i in range(6, n + 1):
        dp[i] = min(dp[i - 3] + 1, dp[i - 5] + 1);

    print(dp[n] if dp[n] != math.inf else -1);