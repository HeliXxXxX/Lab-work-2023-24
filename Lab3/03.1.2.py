A = "AbcdE"

i = 0
capitalLetters = ""
evenpossLetters = ""
novovels = ""
vovels = ["a","e","i","o","u"]

while i < len(A):

    if A[i] == A[i].upper():
        capitalLetters += A[i] + ","

    if i % 2 != 0:
        evenpossLetters += A[i] + ","

    if A[i] == vovels:
        A[i] = "_"
        novovels += A[i] 
    else:
        novovels 

    i += 1
    

print(capitalLetters)
print(evenpossLetters)