def solution(s):
    new = ''
    arr = s.split(' ')
    print(arr)
    for i in range(len(arr)):
        if arr[i] == '':
            new += arr[i]
        elif arr[i][0].isupper() == False:
            new += arr[i][0].upper() + arr[i][1:].lower()
        else:
            new += arr[i]
        
        if i == len(arr)-1:
            break
        else:
            new += ' '
        
    return new

print(solution(" hello m y friend  "))

# 테스트 3
# 입력값 〉 " 2v 3hello m y friend 23HIz "
# 기댓값 〉 " 2v 3hello M Y Friend 23hiz "
# 실행 결과 〉 테스트를 통과하였습니다.

# 테스트 4
# 입력값 〉 " 2v 3hello m y friend "

# 기댓값 〉 " 2v 3hello M Y Friend "
# 실행 결과 〉 테스트를 통과하였습니다.

# 테스트 5
# 입력값 〉 "3peOple unFollowed me"
# 기댓값 〉 "3people Unfollowed Me"

# 실행 결과 〉 테스트를 통과하였습니다.

# 테스트 6
# 입력값 〉 "3peOple 3unFollowed mE"
# 기댓값 〉 "3people 3unfollowed Me"
# 실행 결과 〉 테스트를 통과하였습니다.

# 테스트 7
# 입력값 〉 " hello m y friend "
# 기댓값 〉 " Hello M Y Friend "
# 실행 결과 〉 테스트를 통과하였습니다.