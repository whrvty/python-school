a,b,c, = map(int, input(). split())
if  a > b and a > c:
    if b > c:
        print(b)
    else:
        print(c)
if b > a and b > c:
    if a > c:
        print(a)
    else:
        print(c)
if c > a and c > b:
    if b > a:
        print(b)
    else:
        print(a)