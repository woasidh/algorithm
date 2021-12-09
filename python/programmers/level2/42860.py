import copy;

answer = None;


def solution(name):
    arr = list(map(lambda x: ord(x) - 65, name));
    m, tmpArr = updateArr(arr, 0);
    findNearest(tmpArr, 0, m);
    return answer


def findNearest(arr, start, moved):
    offset = 1;
    didFind = False;
    for i in range(1, len(arr) // 2 + 1):
        right = (start + i) % len(arr)
        left = (start - i) % len(arr)
        if arr[right] != 0 or arr[left] != 0:
            if arr[right] != 0:
                m, tmpArr = updateArr(arr, right);
                findNearest(tmpArr, right, moved + i + m);
            if arr[left] != 0:
                m, tmpArr = updateArr(arr, left);
                findNearest(tmpArr, left, moved + i + m);
            didFind = True;
        if didFind: return;
    global answer;
    if not answer:
        answer = moved;
    else:
        answer = min(answer, moved);


def getAlphabetOffset(num):
    return num if num <= 13 else 26 - num;


def updateArr(arr, idx):
    tmpArr = copy.deepcopy(arr);
    moved = getAlphabetOffset(arr[idx]);
    tmpArr[idx] = 0;
    return (moved, tmpArr);

# https://programmers.co.kr/learn/courses/30/lessons/42860