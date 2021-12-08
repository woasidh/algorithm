from itertools import combinations


def checkUnique(relation, cols):
    s = set([]);
    for i in range(len(relation)):
        t = tuple([relation[i][j] for j in cols]);
        s.add(t);
    return True if len(s) == len(relation) else False;


def checkIncluded(uniques, comb):
    for unique in uniques:
        if set(list(unique)).issubset(set(list(comb))): return True;
    return False;


def solution(relation):
    answer = 0
    col = len(relation[0]);
    unique = [];
    for i in range(1, col + 1):
        combs = list(combinations(list(range(col)), i));
        for comb in combs:
            if checkIncluded(unique, comb): continue;
            if checkUnique(relation, comb):
                unique.append(comb);
    return len(unique);

# https://programmers.co.kr/learn/courses/30/lessons/42890