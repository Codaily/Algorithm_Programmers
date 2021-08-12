import re
def solution(new_id):
    # 1
    new_id = new_id.lower()
    #2
    new_id = re.sub('[\~\!\@\#\$\%\^\&\*\(\)\=\+\[\{\]\}\:\?\,\<\>\/]', '', new_id)
    #3
    new_id = re.sub('[\.]+','.', new_id)
    #4
    new_id = new_id.strip('.')
    #5
    if len(new_id) == 0 :
        new_id += 'a'  
    #6
    new_id = new_id[:15]
    new_id = new_id.strip('.')
    #7
    while len(new_id) < 3 :
        new_id += new_id[-1]
    return new_id

print(solution("abcdefghijklmn.p"))