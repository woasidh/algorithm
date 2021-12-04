import sys

n, m = map(int, sys.stdin.readline().split());
trees = list(map(int, sys.stdin.readline().split()));
trees.sort();

def getTotalLength(trees, height):
    total = 0;
    for tree in trees:
        total += tree - height if tree - height >= 0 else 0;
    return total;

start = 0;
end = trees[-1];

# 6 6 5 5 3 2 1

while start <= end:
    mid = (start + end) // 2;
    if getTotalLength(trees, mid) < m:
        end = mid - 1;
    else:
        start = mid + 1;

print(end);