def merge_sorted(a, b):
    list_ab = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            A = a.pop(0)
            list_ab.append(A)
        else:
            A = b.pop(0)
            list_ab.append(A)
    if not a:
        list_ab.extend(b)
    else:
        list_ab.extend(a)
    return list_ab
list_a = [1,4,9,16]
list_b = [4,7,9,9,11]
print(merge_sorted(list_a, list_b))