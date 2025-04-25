# 45-1
# n = int(input("행 수:"))
# for i in range(n):
#     for j in range(i+1):
#         print("*", end='')
#     print()

#45-2
# n = int(input("행 수:"))
# for i in range(n):
#     for j in range(n-i):
#         print("*", end="")
#     print()

#45-3
# n = int(input("행 수:"))
# for i in range(1, n+1):
#     for j in range(n-i):
#         print(' ', end="")
#     for j in range(i):
#         print("*", end="")
#     print()
    
#45-4
# n = int(input("행 수:"))
# for i in range(n):
#     for j in range(i):
#         print(" ", end="")
#     for k in range(n - i):
#         print("*", end="")
#     print() 

#45-5
n = int(input())
for i in range(n):
    for j in range(n-i-1):
        print(" ", end ="")
    for j in range(i*2+1):
        print("*", end ="")
    print()

#45-6
# n = int(input())

# for i in range(n//2+1):
#     for j in range(n-i-1):
#         print(" ", end ="")
#     for j in range(i*2+1):
#         print("*", end="")
#     print()
# for i in range(n//2,0,-1):
#     for j in range(n-i):
#         print(" ", end ="")
#     for j in range(i*2-1):
#         print("*", end="")
#     print()

