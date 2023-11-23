word_to_search = input("Enter the word you want to search: ").lower()
file_paths = input("Enter file paths separated by a comma ',': ")
file_path = []
A = file_paths.split(",")
for i in A:
    file_path.append(i)

for files in file_path:
    with open(files, "r") as file:
        content = file.read().lower()
        name = file.name
        found_in_file = False
        for line_number, line in enumerate(content.split('\n'), 1):
            if word_to_search in line:
                found_in_file = True
                print(name + ":  " + line)
