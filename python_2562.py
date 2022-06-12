N = []
Max = 0
Number = 0
for _ in range(9):
    N.append(int(input()))

for i in range(len(N)):
    if(Max < N[i]):
        Max = N[i]
        number = i+1
print(Max)
print(number)

