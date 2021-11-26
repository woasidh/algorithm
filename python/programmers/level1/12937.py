def solution(num):
    answer = 'Even' if num % 2 == 0 else 'Odd';
    return answer;

input = [3, 4];

for i in input:
    solution(i);