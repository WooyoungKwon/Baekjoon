import sys

arr = list(sys.stdin.readline().rstrip())
stack = []

def solve():
    for char in arr:
        # 1. 여는 괄호는 스택에 추가
        if char in ('(', '['):
            stack.append(char)
            continue

        # 2. 닫는 괄호 처리
        temp = 0
        
        # 닫는 괄호가 나왔는데 스택이 비어있으면 오류
        if not stack:
            return 0

        while stack:
            top = stack.pop()

            # 스택에서 숫자를 만나면 temp에 더함 (XY 처리)
            if isinstance(top, int):
                temp += top
                continue

            # 짝이 맞는 여는 괄호를 만났을 때
            if char == ')' and top == '(':
                # temp가 0이면 '()', 아니면 '(X)' 형태
                stack.append(2 if temp == 0 else temp * 2)
                break
            
            if char == ']' and top == '[':
                # temp가 0이면 '[]', 아니면 '[X]' 형태
                stack.append(3 if temp == 0 else temp * 3)
                break

            # 짝이 안 맞는 괄호를 만나면 즉시 오류
            return 0
        
        # while문이 break 없이 끝났다면 (짝을 못 찾음) 오류
        else:
            return 0

    # 3. 최종 결과 계산 전 스택 검증
    # 스택에 여는 괄호가 남아있으면 오류
    for item in stack:
        if isinstance(item, str):
            return 0

    # 검증 통과 후 안전하게 합산
    return sum(stack)

print(solve())