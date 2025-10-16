import sys
from collections import Counter

input = sys.stdin.readline
N, K = map(int, input().split())
arr = list(map(int, input().split()))

cnt = dict()

left = 0
right = 0
cnt[arr[right]] = 1
currLen = 1
answer = 0
while True:
    if left >= N - 1 or right >= N - 1:
        break
    if arr[right + 1] not in cnt:
        cnt[arr[right + 1]] = 0
    if cnt[arr[right + 1]] < K:
        cnt[arr[right + 1]] += 1
        right += 1
        currLen += 1
    else:
        cnt[arr[left]] -= 1
        left += 1
        currLen -= 1
    answer = max(answer, currLen)
print(answer)
        