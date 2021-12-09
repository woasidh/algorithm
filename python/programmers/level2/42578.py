def solution(clothes):
    answer = 1
    dic = {};
    for cloth in clothes:
        name, kind = cloth;
        if kind in dic:
            dic[kind] += 1;
        else:
            dic[kind] = 1;
    for count in dic.values():
        answer *= count + 1;

    return answer - 1;

# https://programmers.co.kr/learn/courses/30/lessons/42578