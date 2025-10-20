st = input().rstrip()

answer = 0
isFirst = True
plus = st.split("-")

for p in plus:
    vals = p.split("+")
    res = 0
    for val in vals:
        res += int(val)
    if isFirst:
        isFirst = False
        answer = res
    else:
        answer -= res
print(answer)