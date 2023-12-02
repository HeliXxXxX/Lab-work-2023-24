word_list = {}
def main():
    with open("HeliX_Labs\\Lab7\\07.1.1\\input.txt","r") as input: 
        # change the file path to the pasth of the input file 
        for line in input:
            words = line.split()
            for word in words:
                if word.lower() in word_list:
                    word_list[f"{word.lower()}"] += 1
                else:
                    word_list[f'{word.lower()}'] = 1
    word_list_sorted = dict(sorted(word_list.items(), key=lambda item: item[1], reverse=True))
    max_len = 0
    for wordd in word_list_sorted:
        if len(wordd) > max_len:
            max_len = len(wordd)
    with open('HeliX_Labs\\Lab7\\07.1.1\\output.txt','w') as output: 
        #change this path into the path of a output folder to show the output
        for word, number in word_list_sorted.items():
            output.write(f'{word}')
            if len(word) < max_len:
                A = (max_len +2) - len(word)
            else:
                A = 2
            output.write(" "*A + "- ")
            output.write(str(number))
            output.write('\n')
    print("Run complete")
if __name__ == "__main__":
    main()