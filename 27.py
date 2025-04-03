import random
arr = [1,2,3,4,5,6]
a,a1 = list(map(int, input('2개 입력하세요: ').split()))
b = random.choices(arr, k=2)
print(f"내가 낸 수 = {a,a1}, 컴퓨터가 낸 수 = {b}")

if a == b[0] and a1 == b[1]:
    print("1등")
elif b[0] == a or b[0] == a1 or b[1] == a or b[1] == a1:
    print("2등")
else:
    print("3등")
