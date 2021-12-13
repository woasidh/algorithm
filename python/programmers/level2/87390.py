def solution(n, left, right):
    startRow = left // n;
    startCol = left % n;
    endRow = right // n;
    endCol = right % n;
    answer = [];
    if startRow == endRow:
        return getRow(n, startRow)[startCol:endCol + 1]
    for i in range(startRow, endRow + 1):
        if i == startRow: answer += getRow(n, startRow)[startCol:];
        elif i == endRow: answer += getRow(n, endRow)[:endCol + 1];
        else: answer += getRow(n, i);
    return answer;

def getRow(n, rowNum):
    row = [];
    start = 0;
    while start < n:
        if start < rowNum: row.append(rowNum + 1);
        else: row.append(start + 1);
        start += 1;
    return row;