with open("C:\\Users\\hirun\\OneDrive\\Desktop\\Computer science\\Lab6\\06.1.1\\input.txt", "r") as f:
    n = 0
    for line in f:
        n += 1
        print(f"/*{n}*/ {line.strip()}")