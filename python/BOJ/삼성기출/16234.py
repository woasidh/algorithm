# bfs visited 처리 왜이렇게 못하냐...
# 기본 알고리즘 템플릿 숙지하기

import sys
from collections import deque
import math

n, l, r = map(int, sys.stdin.readline().split());
globalMap = [];
for _ in range(n):
    globalMap.append(list(map(int, sys.stdin.readline().split())));

# bfs로 갱신
# play로

dx = [0, 0, -1, 1];
dy = [1, -1, 0, 0];

def bfs(x, y, visited):
    global globalMap;
    if visited[x][y]: return False;
    s = set([(x, y)]);
    q = deque([(x, y)]);
    visited[x][y] = True;
    while q:
        x, y = q.popleft();
        for i in range(4):
            nx = x + dx[i];
            ny = y + dy[i];
            if not (0 <= nx < n and 0 <= ny < n): continue;
            if visited[nx][ny]: continue;
            if l <= abs(globalMap[x][y] - globalMap[nx][ny]) <= r:
                visited[nx][ny] = True;
                s.add((nx, ny));
                q.append((nx, ny));
    if len(s) == 1: return False;
    average = math.floor(sum([globalMap[pos[0]][pos[1]] for pos in s]) / len(s));
    for (x, y) in s:
        globalMap[x][y] = average;
    return True;

def play():
    visited = [[False] * n for _ in range(n)];
    shouldEnd = True;
    for i in range(n):
        for j in range(n):
            if bfs(i, j, visited): shouldEnd = False;
    return shouldEnd;

answer = 0;
while True:
    if play(): break;
    answer += 1;
print(answer);