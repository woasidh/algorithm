import sys

n, m = map(int, sys.stdin.readline().split());
hashMap = {};
for _ in range(n):
    word = sys.stdin.readline().strip();
    hashMap[word] = False;

answers = [];
for _ in range(m):
    word = sys.stdin.readline().strip();
    if word in hashMap:
        answers.append(word);

answers.sort();
print(len(answers));
for answer in answers:
    print(answer);