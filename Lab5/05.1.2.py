from random import randint

list0 = []
while len(list0) < 10:
    list0.append(randint(1,100))
print(f"Original list {list0}")
print(f"Even index elements {list0[1],list0[3],list0[5],list0[7],list0[9]}")

list2 = []
for n in list0:
    if n % 2==0:
        list2.append(n)
print(f"Even elements {list2}")


print(f"Reverse order {list(reversed(list0))}")

print(f"First and last element {list0[0],list0[-1]}")