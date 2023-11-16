A = "111111111"

i = 0
totalsum = 0
evenvalues = 0
oddvalues = 0
maxvalue = 0
minvalue = 9

while i < len(A):
    totalsum += int(A[i])

    if int(A[i]) % 2 == 0:
        evenvalues = evenvalues +1
    else:
        oddvalues = oddvalues + 1

    if int(A[i]) > maxvalue:
        maxvalue = int(A[i])
    if int(A[i]) < minvalue:
        minvalue = int(A[i])

    i += 1

print(f"the total sum = {totalsum}")
print(f"there are {oddvalues} odd values")
print(f"there are {evenvalues} even values")
print(f"the max value = {maxvalue}")
print(f"the min value = {minvalue}")
