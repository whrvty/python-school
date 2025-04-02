print("1.삼각형, 2.사각형, 3.원")
a = int(input("도형종류:"))
if a==3:
    r = int(input("반지름:"))
else:
    width = int(input("밑변:"))
    height = int(input("높이:"))

if a==1:
    print(f'삼각형의 넓이는 {(width*height)/2}cm^2입니다.')
elif a==2:
    print(f'사각형의 넓이는 {(width*height)}cm^2입니다.')
elif a==3:
    print(f'원의 넓이는 {3.14*r*r}cm^2입니다.')