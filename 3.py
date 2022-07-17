n=input()
s=input()

ans = []

for i in range(0, len(s)):
    j = ord(s[i]) + int(n)
    while j > ord('z'):
        j = j - ord('z') + ord('a') - 1
    ans.append(chr(j))

ans = ''.join(ans)
print(ans)

