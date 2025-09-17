import sys

N, X = map(int, sys.stdin.readline().split())
visitors = list(map(int, sys.stdin.readline().split()))

left = 0
right = X - 1
visitor_count = 0
day = 1
for i in range(left, right + 1):
    visitor_count += visitors[i]

left += 1
right += 1

answer = visitor_count
while right < N:
    visitor_count -= visitors[left - 1]
    visitor_count += visitors[right]
    
    # print(left, right, visitor_count)

    if visitor_count > answer:
        answer = visitor_count
        day = 1

    elif visitor_count == answer:
        day += 1
    
    left += 1
    right += 1

if answer == 0:
    print("SAD")
else:
    print(answer)
    print(day)

    