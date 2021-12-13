def getMultipliedList(l1, l2):
    total = 0;
    for idx, _ in enumerate(l1):
        total += (l1[idx] * l2[idx]);
    return total;


def solution(arr1, arr2):
    answer = [];
    # 1 4  3 3  15 15
    # 3 2  3 3  15 15
    # 4 1       15 15

    n1 = len(arr1);
    n2 = len(arr2);
    n4 = len(arr2[0]);
    for i in range(n1):
        a1 = arr1[i];
        row = [];
        for j in range(n4):
            a2 = [];
            for k in range(n2):
                a2.append(arr2[k][j]);
            row.append(getMultipliedList(a1, a2));
        answer.append(row);

    return answer