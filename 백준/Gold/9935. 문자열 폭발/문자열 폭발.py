import sys

str = "answer"

find = 'n'

str = list(sys.stdin.readline().rstrip())
boom = list(sys.stdin.readline().rstrip())

stack = []
for i in range(len(str)):
    stack.append(str[i])
    if stack[-1] == boom[-1]:
        if stack[len(stack) - len(boom):] == boom:
            for j in range(len(boom)):
                stack.pop()

if stack:
    print(''.join(stack))
else:
    print("FRULA")
