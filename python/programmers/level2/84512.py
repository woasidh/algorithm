import sys
from bisect import bisect_left
from itertools import product

sys.setrecursionlimit(1000000);

alphabets = ['A', 'E', 'I', 'O', 'U'];
dictionary = [];

def solution(word):
    answer = 0
    for length in range(1, 6):
        for set in product(alphabets, repeat = length):
            dictionary.append(''.join(list(set)));
    dictionary.sort();
    return bisect_left(dictionary, word) + 1;