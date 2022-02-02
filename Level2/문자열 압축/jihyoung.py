def solution(s):
    totalLength=[len(s)]
    for size in range(1, len(s)):
        shorten = ""
        split = [s[i:i+size] for i in range(0, len(s), size)]

        count = 1
        for j in range(1, len(split)):
            
            prev, curr = split[j-1], split[j]
            if prev == curr:
                count += 1
            else:
                shorten += (str(count) + prev) if count > 1 else prev
                count = 1

        shorten += (str(count) + split[-1]) if count > 1 else split[-1]
        totalLength.append(len(shorten))

    return min(totalLength)

s = 'abcabcdede'
print(solution(s))