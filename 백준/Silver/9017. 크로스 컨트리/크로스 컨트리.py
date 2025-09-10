import sys

T = int(sys.stdin.readline().rstrip())

def solve():
    # team = [[] for _ in range()]
    N = int(sys.stdin.readline().rstrip())
    team_seq = list(map(int, sys.stdin.readline().rstrip().split()))
    team_count = max(team_seq)

    isTeam = [0] * 201

    for i in range(N):
        isTeam[team_seq[i]] += 1

    ranking = [[] for i in range(201)]

    rank = 1
    for i in range(N):
        if isTeam[team_seq[i]] < 6:
            ranking[team_seq[i]].append(sys.maxsize)
            continue
        ranking[team_seq[i]].append(rank)
        rank += 1

    winner = sys.maxsize
    min_score = sys.maxsize
    for i in range(1, team_count + 1):
        if isTeam[i] < 6:
            continue
        score = sum(ranking[i][:4])
        if min_score > score:
            min_score = score
            winner = i
        elif min_score == score:
            if ranking[winner][4] > ranking[i][4]:
                min_score = score
                winner = i
            elif ranking[winner][4] == ranking[i][4]:
                if ranking[winner][5] > ranking[i][5]:
                    min_score = score
                    winner = i
    return winner

            

for _ in range(T):
    print(solve())