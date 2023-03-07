def solution(keymap, targets):
    click = dict()
    result = list()

    for key in keymap:
        for index, char in enumerate(key):
            click[char] = min(index, click.get(char, float('inf')))

    for target in targets:
        answer = 0
        for char in target:
            if char in click: answer += click[char] + 1
            else:
                answer = -1
                break
        result.append(answer)

    return result
