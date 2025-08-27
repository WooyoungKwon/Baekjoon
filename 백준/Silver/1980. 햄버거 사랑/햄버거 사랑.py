import sys

N, M, T = map(int, sys.stdin.readline().rstrip().split())

maxTime = max(N, M)
minTime = min(N, M)

hambuger = 0
coke = T
for i in range(T // maxTime + 1):
    remaining_time = T - i * maxTime
    curr_hambuger = remaining_time // minTime
    remaining_time -= minTime * curr_hambuger
    curr_hambuger += i
    # print(remaining_time)

    curr_coke = remaining_time
    
    if curr_coke < coke:
        coke = curr_coke
        hambuger = curr_hambuger
        
    elif curr_coke == coke:
        if curr_hambuger > hambuger:
            hambuger = curr_hambuger
    

print(hambuger, coke)
