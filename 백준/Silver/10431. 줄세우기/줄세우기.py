import sys

# 돌의 개수 N을 입력받습니다.
T = int(sys.stdin.readline())
for _ in range(T):
    cnt = 0
    students = list(map(int, sys.stdin.readline().split()))
    for i in range(2, 21):
        for j in range(1, i):
            if students[i] < students[j]:
                tmp = students[i]
                for k in range(i - 1, j - 1, -1):
                    students[k + 1] = students[k]
                    cnt += 1
                students[j] = tmp

    print(students[0], cnt)