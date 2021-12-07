import sys
from collections import deque
n = int(sys.stdin.readline());

def bfs(graph, start):
    if visited[start]: return True;
    q = deque([]);
    flag[start] = 0;
    q.append(start);
    visited[start] = True;

    while q:
        node = q.popleft();
        currentFlag = flag[node];
        targetFlag = 1 - currentFlag;
        for i in graph[node]:
            if flag[i] == -1: flag[i] = targetFlag;
            elif flag[i] == targetFlag: continue;
            else:
                return False;
            if not visited[i]:
                q.append(i);
                visited[i] = True;

    return True;

def isBiGraph(graph):
    for i in range(v + 1):
        if not bfs(graph, i): return False;
    return True;

for _ in range(n):
    # 테스트 케이스 시작
    v, e = map(int, sys.stdin.readline().split());
    graph = [[] for i in range(v + 1)];
    flag = [-1 for i in range(v + 1)];
    visited = [False for i in range(v + 1)];
    for _ in range(e):
        v1, v2 = map(int, sys.stdin.readline().split());
        graph[v1].append(v2);
        graph[v2].append(v1);
    print('YES' if isBiGraph(graph) else 'NO');
