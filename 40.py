import random

for _ in range(100):
    a = random.randint(1, 100)
    b = random.randint(1, 100)

    if a == b:
        print(a)
        break
    else:
        start = min(a, b)
        end = max(a, b)
        hap = 0
        for i in range(start, end + 1):
            hap += i
        print(f"{start}~{end}=>{hap}")