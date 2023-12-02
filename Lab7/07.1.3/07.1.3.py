key = {
    'A': 'Q', 'B': 'W', 'C': 'E', 'D': 'R', 'E': 'T', 'F': 'Y',
    'G': 'U', 'H': 'I', 'I': 'O', 'J': 'P', 'K': 'A', 'L': 'S',
    'M': 'D', 'N': 'F', 'O': 'G', 'P': 'H', 'Q': 'J', 'R': 'K',
    'S': 'L', 'T': 'Z', 'U': 'X', 'V': 'C', 'W': 'V', 'X': 'B',
    'Y': 'N', 'Z': 'M',
    'a': 'q', 'b': 'w', 'c': 'e', 'd': 'r', 'e': 't', 'f': 'y',
    'g': 'u', 'h': 'i', 'i': 'o', 'j': 'p', 'k': 'a', 'l': 's',
    'm': 'd', 'n': 'f', 'o': 'g', 'p': 'h', 'q': 'j', 'r': 'k',
    's': 'l', 't': 'z', 'u': 'x', 'v': 'c', 'w': 'v', 'x': 'b',
    'y': 'n', 'z': 'm', " ": " "
}

def encrypt(input_string):
    new_str = ''
    for i in input_string:
        new_str += key.get(i)
    print(new_str)

def decrypt(input_string):
    new_str = ''
    for i in input_string:
        for x, y in key.items():
            if y == i:
                new_str += x
                break
        else:
            print("character missing in key")
    print(new_str)

encrypt("Hello")
decrypt("Itssg")


