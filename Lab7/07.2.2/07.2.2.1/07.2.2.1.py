def main():

    def encrypt(input_string):
        new_str = ''
        for i in input_string:
            if i != " ":
                new_str += key_dict.get(i, i)
            else:
                new_str += " "
        return new_str
    
    def decrypt(input_string):
        new_str = ''
        for i in input_string:
            if i == "\n":
                new_str += i
            elif i != " ":
                for x, y in key_dict.items():
                    if y == i:
                        new_str += x
                        break
            else:
                new_str += " "
        return new_str
    
    def output(string):
        with open('HeliX_Labs\\Lab7\\07.2.2\\output.txt','a') as output:
            output.write(string)
            
    #takes valeus from the key input file
    letter_list = []
    with open('HeliX_Labs\\Lab7\\07.2.2\\input_key.txt','r') as input:
        for line in input:
            A = line.split()
            for letter in A:
                letter_list.append(letter)
    #turns the values in key file into a dict
    key_dict = {}
    for i in range(0,len(letter_list),2):
        key_dict[letter_list[i]] = letter_list[i+1]

    #writes output into output file
    with open('HeliX_Labs\\Lab7\\07.2.2\\07.2.2.1\\input_text.txt','r') as input:
        for line in input:
            if mode == "encrypt":
                output(encrypt(line))
            if mode == "decrypt":
                output(decrypt(line))

if __name__ == "__main__":
    while True:
        A = input("enter 'e' to encrypt and 'd' to decrypt:  ")
        if A.lower() == "e":
            mode = "encrypt"
            break
        elif A.lower() == "d":
            mode = "decrypt"
            break
    main()