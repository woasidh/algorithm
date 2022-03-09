import sys

nums = int(sys.stdin.readline());

def getZeroandOnes(num):
    zeros = [1, 0, 1];
    ones = [0, 1, 1];
    # if num <= 2: return [zeros[num], ones[num]];
    # else:
    for i in range(3, num + 1):
        zeros.append(zeros[i - 2] + zeros[i - 1]);
        ones.append(ones[i - 2] + ones[i - 1]);
    return [zeros[num], ones[num]];

for _ in range(nums):
    num = int(sys.stdin.readline());
    zeros, ones = getZeroandOnes(num);
    print(zeros, ones);