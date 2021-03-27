class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def solution(numbers, hand):
    result = ''
    keypad = [[1,4,7,'*'],[2,5,8,0],[3,6,9,'#']]
    l_loc = [0,3]
    r_loc = [2,3]
    for i in numbers:
        if i in keypad[0]:
            result += 'L'
            l_loc = [0,keypad[0].index(i)]
        elif i in keypad[2] :
            result += 'R'
            r_loc = [2,keypad[2].index(i)]
        else:
            p_left = Point(l_loc[0], l_loc[1]) 
            p_right = Point(r_loc[0], r_loc[1])
            p_now = Point(1, keypad[1].index(i))
            if abs(p_left.x - p_now.x) + abs(p_left.y - p_now.y) > abs(p_right.x - p_now.x) + abs(p_right.y - p_now.y):
                result += 'R'
                r_loc = [1,keypad[1].index(i)]
            elif abs(p_left.x - p_now.x) + abs(p_left.y - p_now.y) < abs(p_right.x - p_now.x) + abs(p_right.y - p_now.y):
                result += 'L'
                l_loc = [1,keypad[1].index(i)]
            else:
                if hand == 'right':
                    result += 'R'
                    r_loc = [1,keypad[1].index(i)]
                elif hand == 'left': 
                    result += 'L'
                    l_loc = [1,keypad[1].index(i)]
    return result

print(solution([4,5,0],"right"))