def merge(a, b):
    list_ab = []
    if len(a) > len(b):
        A = a
    else:
        A = b
    for i in range(len(A)):
        try:
            A = a[i]
            list_ab.append(A)
        except IndexError:
            None
        try:
            A = b[i]
            list_ab.append(A)
        except IndexError:
            None
    return list_ab
list_a = [1,4,9,16]
list_b = [9,7,4,9,11]
print(merge(list_a,list_b))