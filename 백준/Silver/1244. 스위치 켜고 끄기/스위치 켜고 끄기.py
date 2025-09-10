import sys

switch_count = int(sys.stdin.readline().rstrip())
switch_status = list(map(int, sys.stdin.readline().rstrip().split()))
student_count = int(sys.stdin.readline().rstrip())

students = [list(map(int, sys.stdin.readline().rstrip().split()))
            for _ in range(student_count)]

def man(start):
    idx = start
    while idx - 1 < switch_count:
        switch_status[idx - 1] = int(not switch_status[idx - 1])
        idx += start

def girl(start):
    switch_status[start - 1] = int(not switch_status[start - 1])
    left = (start - 1) - 1
    right = (start - 1) + 1
    while left >= 0 and right < switch_count:
        if switch_status[left] == switch_status[right]:
            switch_status[left] = int(not switch_status[left])
            switch_status[right] = int(not switch_status[right])
        else:
            break
        left -= 1
        right += 1

for s in students:
    if s[0] == 1:
        man(s[1])
    elif s[0] == 2:
        girl(s[1])
print_count = 0
for s in switch_status:
    print(s, end=" ")
    print_count += 1
    if print_count % 20 == 0:
        print()