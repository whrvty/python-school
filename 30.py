sum = 0 
count = 0
score = 0
while True:
    score = float(input())
    if score == -1:
        print("반복종료")
        break
    sum += score
    count += 1
    avg = sum/count
print("="*10)
print(f"합계 : {sum:.1f}")
print(f"평균 : {avg:.1f}")
