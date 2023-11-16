list0 = []
typing = True
total_sum = 0

while typing:
    A = input("Enter a number: ")
    if A == "":
        typing = False
    else:
        list0.append(A)

for index, item in enumerate(list0):
    if index %2== 0:
        total_sum += int(item)
    else:
        total_sum -= int(item)

print(total_sum)

