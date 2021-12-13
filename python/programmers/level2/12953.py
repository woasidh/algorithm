def solution(arr):
    answer = arr[0];
    for i in range(1, len(arr)):
        print(answer, arr[i]);
        answer = getLCM(answer, arr[i]);
    return answer;

def getLCM(n1, n2):
    for i in range(1, (n1 * n2) + 1):
        if i % n1 == 0 and i % n2 == 0:
            return i;