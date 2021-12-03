# dfs
import sys
from collections import deque

n, m, start = map(int, sys.stdin.readline().split());
graph = [[] for _ in range(0, n + 1)];

for _ in range(0, m):
    n1, n2 = list(map(int, sys.stdin.readline().split()));
    graph[n1].append(n2);
    graph[n2].append(n1);

for arr in graph:
    arr.sort();

def dfs(graph, start, visited):
    if (visited[start]): return;
    print(start, end = ' ');
    visited[start] = True;

    for nodeIdx in graph[start]:
        dfs(graph, nodeIdx, visited);

def runDfs(graph, start):
    visited = [False] * (len(graph));
    dfs(graph, start, visited);

def bfs(graph, start, visited):
    q = deque([]);
    q.append(start);

    while q:
        node = q.popleft();
        if (visited[node]): continue;
        visited[node] = True;
        print(node, end = ' ');
        for nodeIdx in graph[node]:
            q.append(nodeIdx);

def runBfs(graph, start):
    visited = [False] * (len(graph));
    bfs(graph, start, visited);

runDfs(graph, start);
print();
runBfs(graph, start);



