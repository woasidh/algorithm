def solution(brown, yellow):
    total = brown + yellow;
    for i in range(1, total + 1):
        if total % i == 0:
            j = total // i;
            if i >= j and 2 * (i + j) - 4 == brown:
                return [i, j];

# https://programmers.co.kr/learn/courses/30/lessons/42842