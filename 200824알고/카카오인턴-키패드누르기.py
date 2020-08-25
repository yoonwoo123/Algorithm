numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"

keypads = {}
num = 1
for x in range(3):
    for y in range(3):
        keypads[num] = [x, y]
        num += 1
keypads['*'] = [3, 0]
keypads[0] = [3, 1]
keypads['#'] = [3, 2]

def solution(numbers, hand):
    left, right = '*', '#'
    answer = ''
    for num in numbers:
        print(num, left, right)
        if num in [1, 4, 7]:
            answer += 'L'
            left = num
        elif num in [3, 6, 9]:
            answer += 'R'
            right = num
        else:
            x, y = keypads[num][0], keypads[num][1]
            lx, ly = keypads[left]
            rx, ry = keypads[right]
            leftDiff = abs(lx - x) + abs(ly - y)
            rightDiff = abs(rx - x) + abs(ry - y)
            if leftDiff > rightDiff:
                answer += 'R'
                right = num
            elif leftDiff < rightDiff:
                answer += 'L'
                left = num
            else:
                if hand == 'right':
                    answer += 'R'
                    right = num
                else:
                    answer += 'L'
                    left = num
    return answer

print(solution(numbers, hand))