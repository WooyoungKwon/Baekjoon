import sys

wheels = [[] for _ in range(5)]
for i in range(1, 5):
    wheels[i] = list(sys.stdin.readline().rstrip())

K = int(sys.stdin.readline().rstrip())
# [회전 톱니바퀴, 방향]
# -1: 반시계방향 1: 시계방향
plans = [list(map(int, sys.stdin.readline().rstrip().split())) 
         for _ in range(K)]

# 12시 방향 = 배열의 첫번째 자리

# 시계방향 회전
def rotateRight(wheel):
    result = []
    result.append(wheel[-1])
    for i in range(len(wheel) - 1):
        result.append(wheel[i])

    return result

def rotateLeft(wheel):
    result = []
    for i in range(1, len(wheel)):
        result.append(wheel[i])
    result.append(wheel[0])

    return result

def print_wheels():
    for w in wheels:
        print(w)
    print()

for number, direction in plans:

    rotate_plan = [0] * 5
    rotate_plan[number] = direction

    rotate_direction = direction
    for i in range(number - 1, 0, -1):
        if wheels[i][2] == wheels[i + 1][6]:
            break
        if wheels[i][2] != wheels[i + 1][6]:
            rotate_direction = 1 if rotate_direction == -1 else -1
            rotate_plan[i] = rotate_direction

    rotate_direction = direction
    for i in range(number + 1, 5):
        if wheels[i - 1][2] == wheels[i][6]:
            break
        if wheels[i - 1][2] != wheels[i][6]:
            rotate_direction = 1 if rotate_direction == -1 else -1
            rotate_plan[i] = rotate_direction

    # print(rotate_plan)

    for i in range(1, 5):
        if rotate_plan[i] == 1:
            wheels[i] = rotateRight(wheels[i])
        elif rotate_plan[i] == -1:
            wheels[i] = rotateLeft(wheels[i])

answer = 0
score = 1
for i in range(1, len(wheels)):
    if wheels[i][0] == "1":
        answer += score
    score *= 2
print(answer)