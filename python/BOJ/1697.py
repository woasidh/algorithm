import sys
from collections import deque
MAX_LIMIT = 100001
n, m = map(int, sys.stdin.readline().split());

visited = [False for i in range(MAX_LIMIT)];
q = deque([]);
q.append((n, 0));
visited[n] = True;

answer = None;

while q:
    num, count = q.popleft();
    if num == m:
        answer = count if answer == None else min(answer, count);
    for i in range(3):
        if i == 0:
            newNum = num - 1;
        elif i == 1:
            newNum = num + 1;
        else:
            newNum = 2 * num;
        if newNum < 0 or newNum >= MAX_LIMIT: continue;
        
        if visited[newNum]: continue;
        q.append((newNum, count + 1));
        visited[newNum] = True;

print(answer);