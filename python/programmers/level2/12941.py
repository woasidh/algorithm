def solution(A,B):
    A.sort();
    B.sort(reverse = True);
    arr = [x * y for x, y in zip(A, B)];
    return sum(arr);