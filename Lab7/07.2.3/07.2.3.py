values_dict = {}
with open('HeliX_Labs\\Lab7\\07.2.3\\rawdata_2004.txt','r') as data:
    for lines in data:
        line = lines.split()
        var = ""
        n = 1
        while line[n] != "$":
            var += line[n].upper()
            var += " "
            n += 1
        var_2 = var[:-1]
        values_dict[var_2] = line[-1]        
while True:
    A = input("Enter country name:  ").upper()
    if A == "QUIT":
        break
    elif A in values_dict:
        print(F"$ {values_dict[A]}")