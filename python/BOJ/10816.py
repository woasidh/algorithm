import sys
from bisect import bisect_right, bisect_left

n = int(sys.stdin.readline());
arr = list(map(int, sys.stdin.readline().split()));
arr.sort();

m = int(sys.stdin.readline());
targets = list(map(int, sys.stdin.readline().split()));
answer = '';
for target in targets:
    left = bisect_left(arr, target);
    right = bisect_right(arr, target);
    val = right - left;
    answer += str(val)+' ';

print(answer);
