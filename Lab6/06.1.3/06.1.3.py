word_to_search = input("Enter the word you want to search: ").lower()
file_path = ["Lab6\\06.1.3\\input_1.txt", "Lab6\\06.1.3\\input_2.txt", "Lab6\\06.1.3\\input_3.txt"]

for files in file_path:
    with open(files, "r") as file:
        content = file.read().lower()
        name = file.name
        found_in_file = False
        # Split the content into lines and iterate through each line
        for line_number, line in enumerate(content.split('\n'), 1):
            if word_to_search in line:
                found_in_file = True
                print(name + ":  " + line)