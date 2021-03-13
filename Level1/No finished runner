# def solution(participant, completion):

#     for i in completion:
#         participant.remove(i)
#     return participant[0]

def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if  participant[i] != completion[i]:
            return participant[i]
    return participant[-1]
