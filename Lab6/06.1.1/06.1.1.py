with open("C:\\Users\\hirun\\OneDrive\\Desktop\\Computer science\\Lab6\\06.1.1\\input.txt", "r") as f:
    with open("C:\\Users\\hirun\\OneDrive\\Desktop\\Computer science\\Lab6\\06.1.1\\output.txt", "w") as f2:
        n = 0
        for line in f:
            n += 1
            f2.write(f"/*{n}*/ {line.strip()} \n")
