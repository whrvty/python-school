n = int(input("사과의 무게:"))
if 375<=n or 210>n:
    print("판정불가")
elif 300<=n<375:
    print("특")
elif 250<=n<300:
    print("상")
elif 210<=n<250:
    print("보통")