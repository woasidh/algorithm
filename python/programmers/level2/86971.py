# 집합으로 풀기

def solution(n, wires):
    # wires 하나씩 없애기
    # wires 돌면서 parent 배열 구하기
    # 전체 parent 돌면서 비교하기
    answer = 1000;
    for i in range(n - 1):
        newWires = wires[:i] + wires[i + 1:];
        arr = [i for i in range(0, n + 1)];
        for wire in newWires:
            union(wire[0], wire[1], arr);
        for idx, val in enumerate(arr):
            arr[idx] = getParent(idx, arr);
        bundleSet = {};
        for val in arr[1:]:
            if not val in bundleSet:
                bundleSet[val] = 1;
            else:
                bundleSet[val] += 1
        answer = min(answer, abs(list(bundleSet.values())[0] - list(bundleSet.values())[1]))
    return answer;


def union(a, b, parent):
    a = getParent(a, parent);
    b = getParent(b, parent);
    if a < b:
        parent[b] = a;
    else:
        parent[a] = b;


def getParent(a, parent):
    if parent[a] != a:
        parent[a] = getParent(parent[a], parent);
    return parent[a];

# dfs로 풀기
import copy
from collections import deque


def solution(n, wires):
    answer = n;
    graph = [[] for i in range(0, n + 1)];
    for wire in wires:
        n1, n2 = wire;
        graph[n1].append(n2);
        graph[n2].append(n1);
    # 하나씩 지우기
    for wire in wires:
        tmpGraph = copy.deepcopy(graph);
        n1, n2 = wire;
        tmpGraph[n1].remove(n2);
        tmpGraph[n2].remove(n1);
        visited = [False] * (n + 1);
        count1 = bfs(tmpGraph, 1, n, visited);
        count2 = n - count1;
        answer = min(answer, abs(count1 - count2));
    return answer;


def bfs(graph, x, n, visited):
    count = 1;
    q = deque([]);
    if visited[x]: return 0;
    visited[x] = True;
    q.append(x);

    while q:
        node = q.popleft();
        for i in graph[node]:
            if visited[i]:
                continue;
            else:
                q.append(i);
                visited[i] = True;
                count += 1;
    return count;





