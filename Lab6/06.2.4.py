column = int(input("enter no. of columns : "))
row = int(input("enter no. of rows : "))

def table(TO,TE,BO,BE,LO,LE,RO,RE,O,E,TL,TRO,TRE,BLO,BLE,BRO,BRE):
    list_top = []
    n = 0
    while n <= column-1:
        if n == 0:
            list_top.append(TL)
        elif n == column-1:
            if column%2==0:
                list_top.append(TRE)
            else:
                list_top.append(TRO)
        elif n%2==0:
            list_top.append(TO)
        else:
            list_top.append(TE)
        n+=1
    list_bottum = []
    n = 1
    while n <= column:
        if row%2==0:
            if n==1:
                list_bottum.append(BLE)
            elif n==column:
                if column%2==0:
                    list_bottum.append(BRE)
                else:
                    list_bottum.append(BRO)
            elif n%2==0:
                list_bottum.append(BO)
            else:
                list_bottum.append(BE)
        else:
            if n==1:
                list_bottum.append(BLO)
            elif n==column:
                if column%2==0:
                    list_bottum.append(BRO)
                else:
                    list_bottum.append(BRE)
            elif n%2==0:
                list_bottum.append(BE)
            else:
                list_bottum.append(BO)
        n+=1
    list_mid_1 = []
    n = 1
    while n <= column:
        if n==1:
            list_mid_1.append(LO)
        elif n==column:
            if column%2==0:
                list_mid_1.append(RE)
            else:
                list_mid_1.append(RO)
        elif n%2==0:
            list_mid_1.append(E)
        else:
            list_mid_1.append(O)
        n+=1
    list_mid_2 = []
    n = 1
    while n <= column:
        if n==1:
            list_mid_2.append(LE)
        elif n==column:
            if column%2==0:
                list_mid_2.append(RO)
            else:
                list_mid_2.append(RE)
        elif n%2==0:
            list_mid_2.append(O)
        else:
            list_mid_2.append(E)
        n+=1
    list_bottum = []
    n = 1
    while n <= column:
        if row%2==0:
            if n==1:
                list_bottum.append(BLE)
            elif n==column:
                if column%2==0:
                    list_bottum.append(BRO)
                else:
                    list_bottum.append(BRE)
            elif n%2==0:
                list_bottum.append(BO)
            else:
                list_bottum.append(BE)
        else:
            if n==1:
                list_bottum.append(BLO)
            elif n==column:
                if column%2==0:
                    list_bottum.append(BRE)
                else:
                    list_bottum.append(BRO)
            elif n%2==0:
                list_bottum.append(BE)
            else:
                list_bottum.append(BO)
        n+=1
    print(list_top)
    n=1
    while n < row-1:
        print(list_mid_2)
        if n==row-2:
            break
        print(list_mid_1)
        n += 2
    print(list_bottum)
#table("TO", "TE", "BO", "BE", "LO", "LE", "RO", "RE", "O", "E", "TL", "TRO", "TRE", "BLO", "BLE", "BRO", "BRE")
print("\nI")
table(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
print("\nII")
table(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)
print("\nIII")
table(1,0,1,0,1,0,1,0,1,0,1,1,0,1,0,1,0)
print("\nIV")
table(0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0)
print("\nV")
table(0,0,0,0,1,1,1,1,1,0,1,1,1,1,1,1,1)
print("\nVI")