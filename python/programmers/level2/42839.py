from itertools import permutations;


def solution(numbers):
    answer = 0
    arr = list(numbers);
    s = set([]);
    for k in range(1, len(numbers) + 1):
        combs = permutations(arr, k);
        for comb in combs:
            num = int(makeNumFromCombination(comb));
            if isPrime(num): s.add(num);

    return len(s);


def makeNumFromCombination(comb):
    str = '';
    for val in comb:
        str += val;
    return str;


def isPrime(num):
    if num == 0 or num == 1: return False;
    for i in range(2, int(num ** (1 / 2)) + 1):
        if num % i == 0: return False;
    return True;