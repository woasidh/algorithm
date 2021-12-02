def solution(n, lost, reserve):
    answer = 0

    total = [-1];

    for i in range (1, n + 1):
        total.append(1);

    for i in lost:
        total[i] -= 1;
    for i in reserve:
        total[i] += 1;

    for idx, i in enumerate(total):
        if i == -1:
            continue;
        if i != 2:
            continue;
        if idx == 1:
            checkRight(total, idx);
        elif idx == n:
            checkLeft(total, idx);
        else:
            if checkLeft(total, idx) != True:
                checkRight(total, idx);

    for i in total:
        if i >= 1:
            answer += 1;
    return answer;

def checkLeft(arr, idx):
    if arr[idx - 1] == 0:
        arr[idx - 1] = 1;
        arr[idx] = 1;
        return True;
    return False;

def checkRight(arr, idx):
    if arr[idx + 1] == 0:
        arr[idx + 1] = 1;
        arr[idx] = 1;
        return True;
    return False;

print(solution(5, [2, 4], [1, 3, 5]));