import sys
k, n = list(map(int, sys.stdin.readline().split()));
nums = list(map(int, sys.stdin.readline().split()));

arr = [];
for num1 in nums:
    for num2 in nums:
        arr.append(num1 * num2);

arr.sort();
print(arr);