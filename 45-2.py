45-2
n = int(input("행 수:"))
for i in range(n):
    for j in range(n-i):
        print("*", end="")
    print()