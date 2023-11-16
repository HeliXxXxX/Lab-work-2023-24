def remove_min(v):
    v.sort()
    v.pop(0)
    
    return v

A = remove_min([1,4,6,8,6,5,0])
print(A)

    



