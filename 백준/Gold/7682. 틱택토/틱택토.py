import sys
from collections import deque, defaultdict

input = sys.stdin.readline

while True:
    ttt = input().rstrip()
    if ttt == "end":
        break

    board = []
    for i in range(0, 9, 3):
        tmp = []
        for j in range(3):
            tmp.append(ttt[i + j])
        board.append(tmp)
    x_complete = 0
    o_complete = 0
    for i in range(3):
        if "X" == board[i][0] == board[i][1] == board[i][2]:
            x_complete += 1
        elif "O" == board[i][0] == board[i][1] == board[i][2]:
            o_complete += 1
        if "X" == board[0][i] == board[1][i] == board[2][i]:
            x_complete += 1
        elif "O" == board[0][i] == board[1][i] == board[2][i]:
            o_complete += 1
    if "X" == board[0][0] == board[1][1] == board[2][2]:
        x_complete += 1
    elif "O" == board[0][0] == board[1][1] == board[2][2] != ".":
        o_complete += 1
    if "X" == board[0][2] == board[1][1] == board[2][0] != ".":
        x_complete += 1
    elif "O" == board[0][2] == board[1][1] == board[2][0] != ".":
        o_complete += 1
    o_cnt = ttt.count("O")
    x_cnt = ttt.count("X")
    # 꽉 차 있을 때
    if "." not in ttt:
        # X가 이기는 경우
        # print(ttt, x_complete, o_complete, x_cnt, o_cnt)
        if x_complete > o_complete and o_complete == 0 and x_cnt - 1 == o_cnt:
            print("valid")
        # O가 이기는 경우
        elif x_complete < o_complete and x_complete == 0 and x_cnt == o_cnt:
            print("valid")
        # 비기는 경우
        elif x_complete == 0 and o_complete == 0 and x_cnt - 1 == o_cnt:
            print("valid")
        else:
            print("invalid")
    # 빈 칸이 있을 때
    else:
        # X가 이기는 경우
        if x_complete > o_complete and x_cnt - 1 == o_cnt:
            print("valid")
        # O가 이기는 경우
        elif o_complete > x_complete and x_cnt == o_cnt:
            print("valid")
        # 진행 중인 경우
        # elif x_complete == 0 and o_complete == 0 and (x_cnt == o_cnt or x_cnt - 1 == o_cnt):
        #     print("valid")
        else:
            print("invalid")
