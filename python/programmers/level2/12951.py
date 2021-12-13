def solution(s):
    # qa a    a  a    a
    answer = '';
    a = 1;
    print(a);

    idx = 0;
    for char in s:
        if char == ' ':
            idx = 0;
        else:
            if idx == 0:
                char = char.upper();
            else:
                char = char.lower();
            idx += 1;
        answer += char;

    return (answer);