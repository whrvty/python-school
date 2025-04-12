cnt = 0
sum = 0

while True:
    try:
        n = int(input("점수:"))
        sum += n
        cnt += 1
    except:
        print(f"합계:{sum:.1f}")
        print(f"평균:{sum/cnt}")
        break