#vowel counter
def vowel_counter(string):
    vowels = 0
    for letter in string:
        if letter.lower() == "a" or letter.lower() =="o" or letter.lower() =="i" or letter.lower() =="e" or letter.lower() =="u":
            vowels += 1
    print(f"There are {vowels} vovels")

vowel_counter("Hello AAAAA")

