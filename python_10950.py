n = int(input())
lst = []

for i in range(n):
    a,b = map(int,input().split())
    lst.append(a+b)

for i in range(n):
    print(lst[i])        