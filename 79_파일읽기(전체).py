f = open("data1.txt", "r")

while True:
    line = f.readline()
    if line == "":
        break
    else:
        print(line, end="")
    
f.close()