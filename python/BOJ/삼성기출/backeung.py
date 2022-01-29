inputs = [
[1, 7, 8],
[1, 9, 10],
[2, 17, 18],
[2, 19, 20]
];

storage = [[], [0, 0, 0], [0, 0, 0]];

for input in inputs:
    idx, c2, c3 = input;
    storage[idx][0] += c2;
    storage[idx][1] += c3;
    storage[idx][2] += 1;

for i in range(1, 3):
    storage[i][0] /= storage[i][2];
    storage[i][1] /= storage[i][2];

print(storage);