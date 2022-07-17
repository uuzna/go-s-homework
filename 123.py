lis = list(input().split('='))
left = list(lis[0])
right = list(lis[1])
k = 0
b = 0
ans = 0
bianliang = 'a'
num = []
for i in range(0, len(left)):
    if (ord(left[i]) >= 48) and (ord(left[i]) <=57):
        num.append(left[i])
    elif (left[i] == '-') or (left[i] == '+'):
        if num!=[] and num != ['-'] and num != ['+']:
            num = ''.join(num)
            b += int(num)
        num = []
        num.append(left[i])
    else:
        bianliang = left[i]
        if num == [] or num == ['+']:
            k += 1
        elif num == ['-']:
            k -= 1
        else:
            num = ''.join(num)
            k += int(num)
            num = []
    if i==(len(left)-1):
        if num != []:
            num = ''.join(num)
            b += int(num)
        num = []

for i in range(0, len(right)):
    if (ord(right[i]) >= 48) and (ord(right[i]) <=57):
        num.append(right[i])
    elif (right[i] == '-') or (right[i] == '+'):
        if num!=[] and num != ['-'] and num != ['+']:
            num = ''.join(num)
            b -= int(num)
        num = []
        num.append(right[i])
    else:
        bianliang = right[i]
        if num == [] or num == ['+']:
            k -= 1
        elif num == ['-']:
            k += 1
        else:
            num = ''.join(num)
            k -= int(num)
            num = []
    if i==(len(right)-1):
        if num != []:
            num = ''.join(num)
            b -= int(num)
        num = []

ans =  - b / k
if ans == -0:
    ans = 0
print("%s=%.3f"%(bianliang,ans))      