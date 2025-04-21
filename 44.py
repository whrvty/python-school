n = int(input("행수:"))
m = int(input("열수:"))
for i in range(1, n + 1):
    for j in range(1, m + 1):
        print(i * j, end=' ')
    print()
