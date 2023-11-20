with open("C:\\Users\\hirun\\OneDrive\\Desktop\\Computer science\\Lab6\\06.1.2\\input.txt", "r") as input:
    with open("C:\\Users\\hirun\\OneDrive\\Desktop\\Computer science\\Lab6\\06.1.2\\output.txt", "w") as output:
        lines = []
        for line in input:
            lines.append(line.strip())
        lines.reverse()
        for i in lines:
            output.write(i + "\n")