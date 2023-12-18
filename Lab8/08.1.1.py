dict_2 = {5:4,9:2,10:3}
dict_2 = {2:4,5:3,8:5}
list_1  = []

last_value = list(dict_2.values())[-1]
last_key = None
for i, j in dict_2.items():
    if j == last_value:
        last_key = i
        break
print(f"last key : {last_key}")

for i in range(0,last_key+1):
    try:
        list_1.append(dict_2[i])
    except KeyError:
        list_1.append(0)
print(list_1)