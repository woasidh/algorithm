import sys

def getTotal(arr, limit):
    total = 0;
    for i in arr:
        total += i if i <= limit else limit;
    return total;

n = int(sys.stdin.readline());
arr = list(map(int, sys.stdin.readline().split()));
arr.sort();
limit = int(sys.stdin.readline());

# 483 484 489

start, end = 0, max(arr);
while start <= end:
    mid = (start + end) // 2;
    if getTotal(arr, mid) <= limit:
        start = mid + 1;
    else:
        end = mid - 1;

print(end);