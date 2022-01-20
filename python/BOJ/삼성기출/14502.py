# 빨리 풀긴함
# 근데 이거 효율성 맞나 - 맞네

from itertools import combinations
import copy
import sys
from collections import deque;

n, m = map(int, sys.stdin.readline().split());
globalMap = [];
for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()));
    globalMap.append(row);

zeros = [];

for i in range(n):
    for j in range(m):
        if globalMap[i][j] == 0:
            zeros.append((i, j));

dx = [0, 0, -1, 1];
dy = [1, -1, 0, 0];

def bfs(tmpMap, x, y):
    global n, m;
    if not tmpMap[x][y] == 2: return;
    q = deque([]);
    q.append((x, y));
    while q:
        x, y = q.popleft();
        for i in range(4):
            nx = x + dx[i];
            ny = y + dy[i];
            if not (0 <= nx < n and 0 <= ny < m): continue;
            if not tmpMap[nx][ny] == 0: continue;
            tmpMap[nx][ny] = 2;
            q.append((nx, ny));

answer = [];

for combination in combinations(zeros, 3):
    # 1로 채워주기
    tmpMap = copy.deepcopy(globalMap);
    for spot in combination:
        tmpMap[spot[0]][spot[1]] = 1;

    for i in range(n):
        for j in range(m):
            bfs(tmpMap, i, j);

    safeSize = 0;
    for i in range(n):
        for j in range(m):
            if tmpMap[i][j] == 0: safeSize += 1;
    answer.append(safeSize);

print(max(answer));

