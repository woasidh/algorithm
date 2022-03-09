import sys

n = int(sys.stdin.readline());
nums = list(map(int, sys.stdin.readline().split()));

dp = [[0 for _ in range(n)] for i in range(n)];

for start in range(n):
    stack = [];
    for i in range(start, n):
        num = nums[i];
        if not stack:
            stack.append(num);
            dp[start][i] = 1;
        else:
            if num > stack[-1]:
                stack.append(num);
                dp[start][i] = len(stack);
            else:
                stack = [num];
                dp[start][i] = len(stack);

for row in dp:
    print(row);


