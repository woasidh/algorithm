import sys
from bisect import bisect_left
n = int(sys.stdin.readline());
nums = list(map(int, sys.stdin.readline().split()));

arr = [];
for idx, num in enumerate(nums):
    if idx == 0:
        arr.append(num);
        continue;
    if arr[-1] < num:
        arr.append(num);
    elif arr[-1] == num:
        continue;
    else:
        idx = bisect_left(arr, num);
        arr[idx] = num;

print(len(arr));


