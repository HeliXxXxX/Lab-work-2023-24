from random import choice

values = []
max_dict = {}
while len(values) != 20:
    A = choice(range(1,7))
    values.append(A)
print(f'starting values : {values}')
len = 0
for i in range(0,19):
    if values[i] == values[i+1]:
        len += 1
        if i == 18:
            len += 1
            max_dict[i] = len
    elif values[i] != values[i+1]:
        len += 1
        max_dict[i] = len
        len = 0
max = 0
for i, j in max_dict.items():
    if max_dict[i] > max:
        max = max_dict[i]
    elif max_dict[i] < max:
        max_dict[i] = 0
    for i, j in max_dict.items():
        if max_dict[i] > max:
            max = max_dict[i]
        elif max_dict[i] < max:
            max_dict[i] = 0
for i, j in list(max_dict.items()):
    if j == 0:
        del max_dict[i]
first_key, first_value = next(iter(max_dict.items()))
new_dict = {first_key: first_value}
for i, j in new_dict.items():
    if j == 1:
        print("no consecutive numbers :(")
    elif i == 18 and values[-1] == values[-2]:
        values[(i-j)+2] = f"( {values[(i-j)+2]}"
        values[i+1] = f"{values[i+1]} )"
    else:
        values[(i-j)+1] = f"( {values[(i-j)+1]}"
        values[i] = f"{values[i]} )"
print(values)