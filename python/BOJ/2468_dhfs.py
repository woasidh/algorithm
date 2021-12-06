import sys
import copy
sys.setrecursionlimit(100000)
n = int(sys.stdin.readline());
graph = [];
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())));

dx = [0, 0, -1, 1];
dy = [1, -1, 0, 0];
def dfs(graph, x, y, k):
    global count;
    if graph[x][y] <= k: return False;
    graph[x][y] = k;
    for i in range(4):
        nx = x + dx[i];
        ny = y + dy[i];
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] <= k: continue;
            dfs(graph, nx, ny, k);
    return True;

answer = -1;
for i in range(0, max(map(max, graph)) + 1):
    count = 0;
    tmpGraph = copy.deepcopy(graph);
    for j in range(n):
        for k in range(n):
            if dfs(tmpGraph, j, k, i):
                count += 1;
    answer = max(answer, count);
print(answer);