from collections import Counter #중복인 값 활용해야할 때

a,b,c =map(int,input().split())
lists = [a,b,c]
result = Counter(lists)
print(result)

if (a==b) and (a==c)and (b==c):
    print(10000+(a*1000))
elif (a == b) or (a == c) or (b == c) == 1:
    for key,value in result.items():
        if value >=2:
            print(1000+(key*100))
    print()
elif (a!=b) and (a!=c) and (b!=c):
    print(max(a,b,c)*100)
