import math
import sys

n = int(sys.stdin.readline());
nums = [];
for _ in range(n):
    nums.append(int(''.join(sys.stdin.readline().split())));

nums.sort();
answer = 0;
for i in range(n):
    answer += math.fabs(i + 1 - (nums[i]));

print(int(answer));