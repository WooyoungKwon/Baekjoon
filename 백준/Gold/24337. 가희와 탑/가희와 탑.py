import sys

def solve():
    N, A, B = map(int, sys.stdin.readline().rstrip().split())
    if N < A + B - 1:
        print(-1)
        return
    else:
        building = []
        
        if A == 1:
            if N > 1 :
                peak = B
            else: # N=1, A=1, B=1
                peak = 1
            
            building.append(peak)
            
            num_hidden = N - (A + B - 1)
            for _ in range(num_hidden):
                building.append(1)
            
            for i in range(B - 1, 0, -1):
                building.append(i)

        else:
            # 숨은 건물
            for i in range(N - A - (B - 1)):
                building.append(1)
                
            for i in range(1, A):
                building.append(i)
            
            
            
            peak = max(A, B)
            building.append(peak)
        
            for i in range(B-1, 0, -1):
                building.append(i)
        
            if len(building) > N:
                print(-1)
                return
            
        print(*building)

solve()