def solution(numbers, target):
    return recursive(numbers, 0, target);

def recursive(arr, total, target):
    if len(arr) == 0: return 1 if total == target else 0;
    return recursive(arr[1:], total + arr[0], target) + recursive(arr[1:], total - arr[0], target);