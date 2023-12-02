letter_list = []
with open('HeliX_Labs\\Lab7\\07.2.2\\input_key.txt','r') as input:
    for line in input:
        A = line.split()
        for letter in A:
            letter_list.append(letter)
key_dict = {}
for i in range(0,len(letter_list),2):
    key_dict[letter_list[i]] = letter_list[i+1]

def decrypt(input_string):
    new_str = ''
    for i in input_string:
        if i != " ":
            new_str += key_dict.get(i)
        else:
            new_str += " "
        
    return new_str
def encrypt(input_string):
    new_str = ''
    for i in input_string:
        for x, y in key_dict.items():
            if y == i:
                new_str += x
                break
        else:
            new_str += " "
    return new_str
def output(X):
    with open('HeliX_Labs\\Lab7\\07.2.2\\output.txt','a') as output:
        output.write(X)
        output.write('\n')

output(encrypt("Hello world"))
output(decrypt("Pcssi bidsm"))

