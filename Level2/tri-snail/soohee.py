
def solution(n):
    length = (int)((n**2+n)/2)
    arr=[[1]*i for i in range(1,n+1)]
    x,y = 0, 0
    
    for i in range(2,length+1):
        num = i
        for j in range(i):
            if i % 3 ==2 :
                x += 1
            elif i % 3 ==1 :
                y+= 1
            elif i% 3 == 0 :
                x -= 1
                y -= 1
            arr[x][y] = num 
    answer = [0]
    print(arr)
    return answer


solution(4)