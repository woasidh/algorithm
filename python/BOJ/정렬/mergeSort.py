arr = [3, 5, 1, 2, 4, 53, 7, 12, 43, 6];
arr1 = [4, 1, 2, 5, 3];

count = 0;

def mergeSort(arr):
    global count;
    mid = len(arr) // 2;

    if len(arr) <= 1: return arr;

    left = mergeSort(arr[:mid]);
    right = mergeSort(arr[mid:]);

    newArr = [];
    leftP = 0;
    rightP = 0;

    while (leftP < len(left) and rightP < len(right)):
        if left[leftP] < right[rightP]:
            newArr.append(left[leftP]);
            leftP += 1;
        elif right[rightP] < left[leftP]:
            newArr.append(right[rightP]);
            rightP += 1;

    while leftP < len(left):
        newArr.append(left[leftP]);
        leftP += 1;
    while rightP < len(right):
        newArr.append(right[rightP]);
        rightP += 1;

    return newArr;

print(mergeSort(arr));