import copy


# 해답봄..
# 모르겠음...

def solution(n, results):
    winMap = {};
    loseMap = {};
    for i in range(1, n + 1):
        winMap[i] = set([]);
        loseMap[i] = set([]);

    for result in results:
        winP, loseP = result;
        winMap[winP].add(loseP);
        loseMap[loseP].add(winP);

    for i in range(1, n + 1):
        for j in winMap[i]:
            loseMap[j].update(loseMap[i]);
        for j in loseMap[i]:
            winMap[j].update(winMap[i]);

    answer = 0;
    for i in range(1, n + 1):
        if len(loseMap[i]) + len(winMap[i]) == n - 1: answer += 1;

    return answer