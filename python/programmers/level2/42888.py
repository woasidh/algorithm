def solution(records):
    answer = [];
    nameRecords = {};
    result = [];
    for record in records:
        message = parseRecord(record, nameRecords);
        if message: result.append(message);
    for r in result:
        nickname = nameRecords[r[0]];
        answer.append(''.join([nickname, r[1]]));
    return answer;
    # 파싱

    # 기록 uid로 기록
    # 1. enter - 들어왔습니다로 기록
    # 2. leave - 나갔습니다로 기록
    # 3. change - 이름 기록 변경

    # 마지막에 uid에 매칭되는 닉네임으로 모두 변경

    return answer


def parseRecord(command, nameRecord):
    arr = command.split();
    command = arr[0];
    if command == 'Enter':
        nameRecord['#' + arr[1]] = arr[2];
        return ['#' + arr[1], '님이 들어왔습니다.']
    elif command == 'Leave':
        return ['#' + arr[1], '님이 나갔습니다.']
    else:
        nameRecord['#' + arr[1]] = arr[2];
        return False;