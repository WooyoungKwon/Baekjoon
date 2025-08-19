import sys

n = int(sys.stdin.readline())
origin = list(sys.stdin.readline().rstrip())
goal = list(sys.stdin.readline().rstrip())

def toggle(arr, i):
    for j in range(i-1, i+2):
        if(0 <= j < n):
            if arr[j] == "1":
                arr[j] = "0"
            elif arr[j] == "0":
                arr[j] = "1"

def simulation(arr, count):
    for i in range(1, n):
        if arr[i-1] != goal[i-1]:
            toggle(arr, i)
            count += 1
    if arr == goal:
        return count
    else:
        return 100001
# 첫 번째 스위치를 누르지 않은 경우
push_arr = origin.copy()
toggle(push_arr, 0)
no_push_arr = origin.copy()

push_cnt = simulation(push_arr, 1)
no_push_cnt = simulation(no_push_arr, 0)
answer = min(push_cnt, no_push_cnt)

answer = -1 if answer == 100001 else answer
print(answer)