word_dict = {}
def main():
    with open("HeliX_Labs\\Lab7\\07.1.2\\input.txt","r") as input: 
        # change the file path to the pasth of the input file 
        for line in input:
            words = line.split()
            for word in words:
                if word.lower() in word_dict:
                    word_dict[f"{word.lower()}"] += 1
                else:
                    word_dict[f'{word.lower()}'] = 1
    word_dict_sorted = dict(sorted(word_dict.items(), key=lambda item: item[1], reverse=True))
    max_len = 0
    for wordd in word_dict_sorted:
        if len(wordd) > max_len:
            max_len = len(wordd)
    #change this path into the path of a output folder to show the output
    word_dict_sorted.pop("the")
    word_dict_sorted = {key: value for key,value in list(word_dict_sorted.items())[:5]}  
    for i, item in word_dict_sorted.items():
        print(i, item)
    print("Run complete")

if __name__ == "__main__":
    main()