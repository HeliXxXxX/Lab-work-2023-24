attempts = 0
sum = 0
while True:
    A = (input("enter floatvalues"))
    try:
        float(A)
        sum += float(A)
    except ValueError:
        attempts += 1
    if not attempts < 2:
        break
    elif A == "":
        print(f'total = {sum}')
        break