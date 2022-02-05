# 깔끔하게 정리하기

towers = set([1, 2, 3]);

def solution(n):
    answer = []
    str = move(1, 3, n);
    return [[int(str[i]), int(str[i + 1])] for i in range(0, len(str), 2)]

def move(start, end, k):
    if k == 1:
        return ''+str(start)+str(end);
    order = '';
    another = getAnother(start, end);
    order += move(start, another, k - 1);
    order += move(start, end, 1);
    order += move(another, end, k - 1);
    return order;

def getAnother(num1, num2):
    return list(towers - set([num1, num2]))[0];