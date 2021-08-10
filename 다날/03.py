arr = [[1, 4], [2, 6], [5, 7], [4, 7]]

def solution(arr):
    answer = 0
    arr.sort()
    prevMeetingStartTime = 99999999

    for i in range(len(arr) - 1, -1, -1):
        meetingStartTime, meetingEndTime = arr[i]

        if meetingEndTime <= prevMeetingStartTime:
            answer += 1
            prevMeetingStartTime = meetingStartTime

    return answer

print(solution(arr))