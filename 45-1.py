# 45-1
n = int(input("행 수:"))
for i in range(n):
    for j in range(i+1):
        print("*", end='')
    print()