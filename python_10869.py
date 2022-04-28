a,b = input().split() #한번에 값 두개 입력받기

a= int(a)
b= int(b)

if a >=1 and b <= 10000:
    print(a+b)
    print(a-b)
    print(a*b)
    print(a//b) #나누기는 /가 아닌 // 으로
    print(a%b)
