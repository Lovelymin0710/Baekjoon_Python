N = int(input())

s = []

for i in range(0,N):
    a = int(input())
    s.append(a)

s.sort()
print(s)
for j in range(len(s)):
    print(s[j])

    