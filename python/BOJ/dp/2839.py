import sys
import math

sys.setrecursionlimit(10000);

n = int(sys.stdin.readline());
dp = [math.inf for _ in range(n + 1)];

def getMinBag(weight):
    if weight <= 0: return math.inf;
    if weight == 3 or weight == 5: return 1;
    if dp[weight] != math.inf:
        return dp[weight];
    else:
        value = min(getMinBag(weight - 3) + 1, getMinBag(weight - 5) + 1);
        dp[weight] = value;
        return value;


answer = getMinBag(n);
print(answer if answer != math.inf else -1);