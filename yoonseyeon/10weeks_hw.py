inFp = None
inStr = ""

inFp = open("C:\\Users\\ysy\\Desktop\\python실습\\.dist\\FileTest\\data1.txt", "r", encoding='UTF8')

cnt = 1

while True:
    inStr = inFp.readline()
    if inStr == "":
        break
    print("%d: %s" % (cnt, inStr), end="")
    cnt += 1

inFp.close()
