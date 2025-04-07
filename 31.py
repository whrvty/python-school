import random
a = list(range(1, 21))
b = random.choice(a)
while True:
    n = int(input())
    if n == b:
        print('완료')
        break
    elif n > b:
        print("더 작은 수")
    elif n < b:
        print("더 큰 수")