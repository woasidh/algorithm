import heapq

INF = int(1e9)


def solution(N, roads, K):
    answer = 0
    graph = [[] for i in range(N + 1)];
    # 각 리스트로 저장
    for road in roads:
        start, end, dist = road;
        graph[start].append((end, dist));
        graph[end].append((start, dist));
    # 힙 큐로 최신화
    minDistInfos = [INF] * (N + 1);
    minDistInfos[1] = 0;
    hq = [];
    heapq.heappush(hq, (1, 0));
    while hq:
        node, dist = heapq.heappop(hq);
        for info in graph[node]:
            end, dist = info;
            if minDistInfos[end] > minDistInfos[node] + dist:
                minDistInfos[end] = minDistInfos[node] + dist;
                heapq.heappush(hq, (end, minDistInfos[node] + dist));
    for i in minDistInfos[1:]:
        if i <= K: answer += 1;

    # 각 배열값으로 k계산

    return answer