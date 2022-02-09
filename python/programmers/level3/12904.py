def solution(s):
    answers = [];
    for idx, _ in enumerate(s):
        length = 1;
        offset = 1;
        # 홀수일 때
        while True:
            if idx - offset < 0 or idx + offset >= len(s): break;
            if s[idx - offset] == s[idx + offset]:
                offset += 1;
                length += 2;
            else: break;
        answers.append(length);
        length = 0;
        offset = 1;
        # 짝수 일 때
        while True:
            if idx - offset < 0 or idx + offset - 1 >= len(s): break;
            if s[idx - offset] == s[idx + offset - 1]:
                offset += 1;
                length += 2;
            else: break;
        answers.append(length);

    return max(answers);