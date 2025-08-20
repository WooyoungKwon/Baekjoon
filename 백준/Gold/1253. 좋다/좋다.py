import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()

def isGood(i, left, right):
    while(left < right):
        if left == i:
            left += 1
            continue
        if right == i:
            right -= 1
            continue
            
        
        currSum = arr[left] + arr[right]
        if arr[i] == currSum:
            return True
        if currSum < arr[i]:
            left += 1
        elif currSum > arr[i]:
            right -= 1
    return False

def isFinalGood(i, left, right):
    while(left < right):
        currSum = arr[left] + arr[right]
        if arr[i] == currSum:
            return True
        if currSum < arr[i]:
            left += 1
        elif currSum > arr[i]:
            right -= 1
    return False

count = 0

# 맨 왼쪽
if isFinalGood(0, 1, n - 1):
    count += 1

# 맨 오른쪽
if isFinalGood(n - 1, 0, n - 2):
    count += 1


if n > 2:
    for i in range(1, n - 1):
        if isGood(i, 0, n-1):
            count += 1
print(count)

    

    