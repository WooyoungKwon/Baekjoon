import sys

# dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

N = int(sys.stdin.readline().rstrip())
numbers = list(map(int,sys.stdin.readline().rstrip().split()))
operator = list(map(int,sys.stdin.readline().rstrip().split()))

ex = []
ex.append(numbers[0])

def calc():
    result = 0
    oper = 0
    for i in range(len(ex)):
        if i % 2 == 0:
            if oper == 0:
                result += ex[i]
            elif oper == 1:
                result -= ex[i]
            elif oper == 2:
                result *= ex[i]
            elif oper == 3:
                if result < 0:
                    result = ((result * -1) // ex[i]) * -1
                else:
                    result = result // ex[i]
        else:
            oper = ex[i]
    return result

min_answer = sys.maxsize
max_answer = -sys.maxsize
def back(cnt, num):
    global min_answer, max_answer
    if cnt == N - 1:
        result = calc()
        max_answer = max(max_answer, result)
        min_answer = min(min_answer, result)
        return
    for i in range(4):
        if operator[i] > 0:
            ex.append(i)
            ex.append(numbers[num])
            operator[i] -= 1
            back(cnt + 1, num + 1)
            operator[i] += 1
            ex.pop()
            ex.pop()
back(0, 1)
print(max_answer)
print(min_answer)
    

