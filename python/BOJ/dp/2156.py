# fuck...

import sys

n = int(sys.stdin.readline());
nums = [];
for _ in range(n):
    nums.append(int(sys.stdin.readline()));

if n == 1:
    print(nums[0]);
elif n == 2:
    print(sum(nums));
else:
    dp = [[0, 0, 0] for _ in range(n)];
    dp[0] = [0, nums[0], 0];
    dp[1] = [nums[0], nums[1], nums[0] + nums[1]];
    for i in range(2, n):
        dp[i][0] = max(dp[i - 1][1], dp[i - 1][2]);
        dp[i][1] = dp[i - 1][0] + nums[i];
        dp[i][2] = dp[i - 1][1] + nums[i];


    print(dp);

    print(max(dp[n - 1]));

