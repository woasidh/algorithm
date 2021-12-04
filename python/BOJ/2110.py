import sys

def countAvailableWifi(arr, offset):
    count = 1;
    prev = arr[0];
    for i in range(1, len(arr)):
        if arr[i] - prev >= offset:
            count += 1;
            prev = arr[i];
    return count;

n, c = list(map(int, sys.stdin.readline().split()));
coordinates = [int(y) for y in sys.stdin.read().splitlines()][:n]
coordinates.sort();
# 1 2 4 8 9

start = 1;
end = coordinates[-1] - coordinates[0];

# 5 3 3 2 2 2 2 2

while start <= end:
    mid = (start + end) // 2;
    availableWifis = countAvailableWifi(coordinates, mid);
    if availableWifis < c:
        end = mid -1;
    else:
        start = mid + 1;

print(end);



