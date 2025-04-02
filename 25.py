a, b = map(int, input(). split())

c = str(a)[0:2]

if b <= 4:
    if b%2==0:
        print(f"현재나이는 {2025-(1900+int(c))+1}입니다.")
        print("여자입니다.")
    else:
        print(f"현재나이는 {2025-(1900+int(c))+1}입니다.")
        print("남자입니다")
else:
    print("존재하지 않습니다.")