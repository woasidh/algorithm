def solution(s):
    return recursive(s)

def recursive(string):
    zeros = 0;
    count = 0;
    while string != '1':
        count += 1;
        newString = '';
        for char in string:
            if char == '1': newString += char;
            else: zeros += 1;
        string = bin(len(newString))[2:];
    return [count, zeros]