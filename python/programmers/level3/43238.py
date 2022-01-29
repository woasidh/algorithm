# ????
# 10분만에 품

def solution(n, counters):
    answer = 0
    maxTime = n * max(counters);
    minTime = 0;
    # 0 1 1 2 2 3 3
    while minTime <= maxTime:
        mid = (minTime + maxTime) // 2;
        if getFinished(counters, mid) >= n:
            maxTime = mid - 1;
        else:
            minTime = mid + 1;
    return minTime;


def getFinished(counters, time):
    finished = 0;
    for counter in counters:
        finished += time // counter;
    return finished;