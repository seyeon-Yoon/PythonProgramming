dan = 2
while dan <= 9:
    print("# " + str(dan) + "단 #", end="\t")
    dan = dan + 1
print()

i = 1
while i <= 9:
    dan = 2
    while dan <= 9:
        result = dan * i

        if result < 10:
            print(str(dan) + "X" + str(i) + "=  " + str(result), end="\t")
        else:
            print(str(dan) + "X" + str(i) + "= " + str(result), end="\t")

        dan = dan + 1
    print()
    i = i + 1