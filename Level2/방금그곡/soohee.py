def note(n):
    if "C#" in n : 
        n = n.replace("C#","c")
    if "D#" in n : 
        n = n.replace("D#","d")
    if "F#" in n : 
        n = n.replace("F#","f")
    if "G#" in n : 
        n = n.replace("G#","g")
    if "A#" in n : 
        n = n.replace("A#","a")
    
    return n

def solution(m, musicinfos):
    answer = []
    music = {}
    m = note(m)
    for mu in musicinfos:
        sound = ""
        mu = mu.split(',')
        length = (int(mu[1][:2]) -int(mu[0][:2])) * 60  + int(mu[1][-2:]) - int(mu[0][-2:]) 
        mu[3] = note(mu[3])

        if length > len(mu[3]) :
            while length > len(sound):
                sound += mu[3]
            sound = sound[:length]
        else :
            sound = mu[3][:length]

        music[mu[2]] = sound
    
    for k,v in music.items():
        if m in v:
            answer.append(k)

    if len(answer) > 1 :
        Max = 0
        k = ""
        for a in answer:
            if Max < len(music[a]):
                Max = len(music[a])
                k = a
        return k
    elif len(answer) == 1:
        return "".join(answer)
    else :
        return "(None)"
         

#                  음      음악이 시작한 시각, 끝난 시각,    음악 제목,     악보 정보
print(solution("CC#BCC#BCC#B",["03:00,03:05,FOO,CC#B","03:00,03:40,ROSE,CC#B","03:00,03:40,POPO,CC#B","03:00,03:50,PPPP,CC#B"]))