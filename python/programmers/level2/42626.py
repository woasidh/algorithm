import heapq


def solution(scoville, K):
    answer = 0

    hq = [];
    for s in scoville:
        heapq.heappush(hq, s);
    while hq[0] < K:
        newS = formula(hq)
        if newS == -1: return -1;
        heapq.heappush(hq, newS);
        answer += 1;

    return answer


def formula(hq):
    if len(hq) < 2: return -1;
    n1 = heapq.heappop(hq);
    n2 = heapq.heappop(hq);
    return n1 + (n2 * 2);