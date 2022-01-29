# 20분 만에 품
# 다익스트라 숙지하기

import heapq
import math


def solution(n, edges):
    answer = 0
    edgeMap = {};
    for i in range(1, n + 1):
        edgeMap[i] = [];
    for edge in edges:
        start, end = edge;
        edgeMap[start].append(end);
        edgeMap[end].append(start);
    distances = getDistances(edgeMap, 1, n);
    distances.sort(reverse=True);
    answer = 0;
    for distance in distances:
        if distance == distances[0]: answer += 1;
    return answer;


def getDistances(edgeMap, start, n):
    hq = [];
    distances = [math.inf for i in range(n + 1)];
    hq.append((0, start));
    distances[start] = 0;
    while hq:
        dist, v = heapq.heappop(hq);
        targets = edgeMap[v];
        for target in targets:
            if dist + 1 < distances[target]:
                distances[target] = dist + 1;
                heapq.heappush(hq, (dist + 1, target));
    del distances[0];
    return distances;