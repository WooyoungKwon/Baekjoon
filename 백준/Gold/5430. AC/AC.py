import sys

def execute(func, arr, n):
    head = 0
    tail = 0
    isHead = 1
    for f in func:
        if f == "R":
            isHead = 1 if isHead == 0 else 0
        elif f == "D" and isHead == 1:
            head += 1
        elif f == "D" and isHead == 0:
            tail += 1
    if head + tail > len(arr):
        return "error"
    if isHead == 1:
        return arr[head:len(arr) - tail]
    else:
        answer = list(arr[head:len(arr) - tail])
        answer.reverse()
        return answer
        

def preProcess(s):
    s = s[1:len(s) - 1]
    return s.split(",")

def answerPrint(s):
    if s == "error":
        print("error")
        return
    if len(s) == 0:
        print("[]")
        return
    if s[0] == '':
        print("[]")
        return
    print("[", end='')
    for i in range(len(s)):
        print(int(s[i]), end='')
        if i != len(s) - 1:
            print(",", end='')
    print("]")

def edgeCase(f, n):
    if n == 0 and "D" in f:
        return True

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    F = sys.stdin.readline().rstrip()
    N = int(sys.stdin.readline().rstrip())
    a = sys.stdin.readline().rstrip()
    if edgeCase(F, N):
        print("error")
        continue
    X = preProcess(a)
    answerPrint(execute(F, X, N))