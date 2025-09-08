import sys

# 돌의 개수 N을 입력받습니다.
# N = int(sys.stdin.readline())
# bigBoys = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

aeiou = ["a", "e", "i", "o", "u"]

while True:
    password = sys.stdin.readline().rstrip()

    if password == "end":
        break

    flag = False

    for a in aeiou:
        if a in password:
            flag  = True

    if not flag:
        print(f"<{password}> is not acceptable.")
        continue

    if len(password) < 2:
        print(f"<{password}> is acceptable.")
        continue

    if len(password) == 2:
        if password[0] == password[1]:
            if password[0] != "e" and password[0] != "o":
                print(f"<{password}> is not acceptable.")
                continue
        print(f"<{password}> is acceptable.")
        continue


    for i in range(len(password) - 1):
        if password[i] == password[i + 1]:
            if password[i] != "e" and password[i] != "o":
                flag = False
                break
        if i < len(password) - 2:
            if password[i] in aeiou:
                if password[i+1] in aeiou and password[i+2] in aeiou:
                    flag = False
                    break
            else:
                if password[i+1] not in aeiou and password[i+2] not in aeiou:
                    flag = False
                    break
        
    if flag:
        print(f"<{password}> is acceptable.")
    else:
        print(f"<{password}> is not acceptable.")