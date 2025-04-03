import random
user = input("가위, 바위 보 중에 하나 입력:")
choices = ["가위", "바위", "보"]
com = random.choice(choices)
print(f"컴퓨터:{com}")
if user == com:
    print("무승부")
elif (user == "가위" and com == "보") or (user == "바위" and com == "가위") or (user == "보" and com == "바위"):
    print("승리")
else:
    print("패배")