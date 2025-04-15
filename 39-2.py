n = int(input('자연수입력:'))
fac = 1
for i in range(1, n+1):
    fac *= i
print(f"{i}!는 {fac}")