import sys

n = int(sys.stdin.readline());
nodeInfo = [False for _ in range(n + 1)];
nodeInfo[1] = True;
for i in range(n - 1):
    a, b = map(int, sys.stdin.readline().split());
    if not nodeInfo[a]:
        nodeInfo[a] = b;
        continue;
    if not nodeInfo[b]:
        nodeInfo[b] = a;
        continue;

for i in range(2, n + 1):
    print(nodeInfo[i]);
