def solution(array, commands):
    answer = []
    arr = []
    i,j,k =0,0,0
    for a in commands:
        i = a[0] ,j = a[1] , k= a[2]
        arr = array[i-1:j]
        arr.sort()
        answer.append(arr[k-1])        
    return answer

solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]])	