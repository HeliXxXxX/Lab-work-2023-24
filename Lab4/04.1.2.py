#word counter 
def word_counter(string):
    words = 1
    for letter in string:
        if letter == " ":
            words += 1
    print(f"there are {words} words")

word_counter("Hello World")