import sys

def solve():
    # N: 현재 랭킹 리스트 점수 개수
    # new_score: 태수의 새로운 점수
    # P: 랭킹 리스트에 올라갈 수 있는 최대 점수 개수
    N, new_score, P = map(int, sys.stdin.readline().split())

    # 1. 랭킹 리스트가 비어있는 경우
    if N == 0:
        print(1)
        return

    score_list = list(map(int, sys.stdin.readline().split()))

    # 2. 랭킹 리스트가 꽉 찼고, 새로운 점수가 꼴찌 점수보다 낮거나 같은 경우
    if N == P and new_score <= score_list[-1]:
        print(-1)
        return

    # 3. 새로운 점수의 순위 계산
    rank = 1
    for i in range(N):
        if new_score < score_list[i]:
            rank += 1
        else:
            # 새로운 점수가 현재 점수보다 크거나 같으면, 순위가 결정됨
            break
            
    print(rank)

solve()