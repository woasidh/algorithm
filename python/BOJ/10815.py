import sys
from bisect import bisect_right

n = int(sys.stdin.readline());
# TODO map이 list 반환하는지?? - iterable한 객체 return
arr = list(map(int, sys.stdin.readline().split()));
arr.sort();

m = int(sys.stdin.readline());
targets = list(map(int, sys.stdin.readline().split()));

for target in targets:
    print (1 if arr[bisect_right(arr, target) - 1] == target else 0, end = ' ');
