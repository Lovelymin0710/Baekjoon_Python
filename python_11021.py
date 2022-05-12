n = int(input())
lst = []

for i in range(n):
    a,b = map(int,input().split())
    lst.append(a+b)

for i in range(0,n):
    print("Case #%d:" %(i+1),lst[i])        