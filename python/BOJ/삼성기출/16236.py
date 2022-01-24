import sys
from collections import deque
import heapq

n = int(sys.stdin.readline());
globalMap = [];
for _ in  range(n):
    globalMap.append(list(map(int, sys.stdin.readline().split())));
shark = None;
sharkSize = 2;
moved = 0;
fishCount = 0;
for i in range(n):
    for j in range(n):
        val = globalMap[i][j];
        if val != 0:
            if val == 9:
                globalMap[i][j] = 0;
                shark = (i, j);

dx = [-1, 0, 0, 1];
dy = [0, -1, 1, 0];

def findNearestFish(x, y, visited):
    # print('dfs 시작', x, y);
    global globalMap, sharkSize;
    q = [(0, x, y)];
    visited[x][y] = True;
    hit = [];
    while q:
        dist, x, y = heapq.heappop(q);
        for i in range(4):
            nx = x + dx[i];
            ny = y + dy[i];
            if not (0 <= nx < n and 0 <= ny < n): continue;
            if visited[nx][ny]: continue;
            val = globalMap[nx][ny];
            if val == 0:
                heapq.heappush(q, (dist + 1, nx, ny));
                visited[nx][ny] = True;
            else:
                if val > sharkSize: continue;
                elif val == sharkSize:
                    heapq.heappush(q, (dist + 1, nx, ny));
                    visited[nx][ny] = True;
                else:
                    visited[nx][ny] = True;
                    heapq.heappush(hit, (dist + 1, nx, ny));
        if (not q or q and q[0][0] > dist) and hit:
            a = heapq.heappop(hit);
            # print(q, hit, a, 'any');
            return a;
        # print(q, dist, hit, 'every');
    return False;

while True:
    visited = [[False] * n for _ in range(n)];
    targetFish = findNearestFish(shark[0], shark[1], visited);
    if not targetFish:
        print(moved);
        break;
    else:
        globalMap[targetFish[1]][targetFish[2]] = 0;
        moved += targetFish[0];
        shark = (targetFish[1], targetFish[2]);
        fishCount += 1;
        if fishCount == sharkSize:
            sharkSize += 1;
            fishCount = 0;

