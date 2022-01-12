# board 정보 저장 x -> x, y 좌표 저장해서 풀기

import sys
import copy
import heapq

def getSlidedRow(row):
    # 빨간색 빠지면 True, 파란색 - False
    length = len(row);
    for i in range(length-1, 0, -1):
        if row[i] == 'R' or row[i] == 'B':
            destIdx = i;
            while True:
                if row[destIdx + 1] == '.': destIdx += 1;
                elif row[destIdx + 1] == '#': break;
                elif row[destIdx + 1] == 'O':
                    if row[i] == 'B': return False;
                    else: return True;
                elif row[destIdx + 1] == 'R' or row[destIdx + 1] == 'B': break;
            row[i], row[destIdx] = row[destIdx], row[i];
    return row;



def tiltMap(globalMap, dir):
    # 빨간색 - True 파란색 - False
    global n, m;
    if dir == 0 or dir == 1:
        for i in range(1, n - 1):
            row = globalMap[i] if dir == 0 else list(reversed(globalMap[i]));
            row = getSlidedRow(row);
            if row == False: return False;
            elif row == True: return True;
            globalMap[i] = row if dir == 0 else list(reversed(row));
    else:
        for i in range(1, m - 1):
            col = [row[i] for row in globalMap] if dir == 2 else [row[i] for row in list(reversed(globalMap))];
            col = getSlidedRow(col);
            if col == False: return False;
            elif col == True: return True;
            for j in range(1, n - 1):
                if dir == 2: globalMap[j][i] = col[j];
                else: globalMap[j][i] = col[(n - 1) - j];
    return globalMap;



def bfs(globalMap):
    hq = [];
    heapq.heappush(hq, (0, globalMap));
    while hq:
        count, board = heapq.heappop(hq);
        if count == 10: continue;
        for i in range(4):
            newBoard = tiltMap(copy.deepcopy(board), i);
            if newBoard == True: return count + 1;
            elif newBoard == False: continue;
            else: heapq.heappush(hq, (count + 1, newBoard));
    return -1;





n, m = map(int, sys.stdin.readline().split());
globalMap = [];
for _ in range(n):
    globalMap.append(list(''.join(sys.stdin.readline().split())));
print(bfs(globalMap));

'''
dfs 저장 데이터
    count
dfs 큐 삽입 안 할 조건
    10번 넘겼을 때
    파란색이 구멍으로 들어갔을 때
dfs 큐 삽입 조건
    10번 이하일 때
dfs 상태 저장
    copy로
    
16 16 16 16 16 
256 256 16

300 300 20
1800000000
'''



