while True:
    n = int(input("입력:"))
    if n == 0:
        print('입력종료')
        break
    elif n%5 == 0:
        print("5의 배수입니다")
    else:
        print("5의 배수가 아닙니다")
    