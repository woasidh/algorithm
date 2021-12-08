def solution(number, k):
    s = [];
    for pullIdx, pulledNum in enumerate(number):
        if k == 0: return ''.join(s) + number[pullIdx:];
        while s and s[-1] < pulledNum and k > 0:
            s.pop();
            k -= 1;
        s.append(pulledNum);
    return ''.join(s[:-1]) if k > 0 else ''.join(s);

# https://programmers.co.kr/learn/courses/30/lessons/42883#