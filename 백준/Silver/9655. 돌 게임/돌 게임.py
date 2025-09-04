import sys

# 돌의 개수 N을 입력받습니다.
N = int(sys.stdin.readline())

# N이 홀수인지 짝수인지 판별합니다.
if N % 2 == 1:
  # N이 홀수이면 상근이가 이깁니다.
  print("SK")
else:
  # N이 짝수이면 창영이가 이깁니다.
  print("CY")