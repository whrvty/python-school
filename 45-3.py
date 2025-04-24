# 45-3
n = int(input("행 수:"))
for i in range(1, n+1):
    for j in range(n-i):
        print(' ', end="")
    for j in range(i):
        print("*", end="")
    print()