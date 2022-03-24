import sys
from bisect import bisect_left

n = int(sys.stdin.readline());
nums = list(map(int, sys.stdin.readline().split()));
m = int(sys.stdin.readline());
targets = list(map(int, sys.stdin.readline().split()));

# targetMap = {};
# for i in range(m):
#     targetMap[targets[i]] = i;
# nums.sort();
# targets.sort();
#
# currentIdx = 0;
# currentTarget = targets[currentIdx];
#
# answers = [0 for _ in range(m)];
#
# for i in range(n):
#     if nums[i] == currentTarget:
#         answers[targetMap[currentTarget]] = 1;
#         currentIdx += 1;
#         if currentIdx == len(targets): break;
#         else: currentTarget = targets[currentIdx];
#
# for answer in answers:
#     print(answer);

nums.sort();

# 1 2 3 4 5
for target in targets:
    idx = bisect_left(nums, target);
    if idx < 0 or idx >= len(nums): print(0);
    elif nums[idx] == target: print(1);
    else: print(0);

