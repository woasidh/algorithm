import sys
from collections import deque
import copy

dx = [0, 0, -1, 1];
dy = [1, -1, 0, 0];

def bfs(graph, x, y, k):
    if graph[x][y] <= k:
        # print('바로 끝');
        return False;
    q = deque([]);
    q.append((x, y));
    graph[x][y] = k;
    while q:
        x, y = q.popleft();
        # print(x, y, '뽑음');
        for i in range(4):
            nx = x + dx[i];
            ny = y + dy[i];
            # print(nx, ny, '훑어본 결과: ', end = ' ');
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                # print('범위 벗어남');
                continue;
            if graph[nx][ny] <= k:
                # print('k이하');
                continue;
            # print('q에 넣음');
            q.append((nx, ny));
            graph[nx][ny] = k;
    # print('끝');
    return True;


n = int(sys.stdin.readline());
graph = [];
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())));

answer = [];
# TODO 2차원 배열에서 max 값 구하는 법
for k in range(max(map(max, graph))):
    print(k);
    count = 0;
    tmpGraph = copy.deepcopy(graph);
    for i in range(n):
        for j in range(n):
            if bfs(tmpGraph, i, j, k): count += 1;
    answer.append(count);

print(max(answer));