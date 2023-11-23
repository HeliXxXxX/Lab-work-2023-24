try:
    with open("Lab6\\06.1.4\\input.txt", "r") as file:
        for line in file:
            list1 = []
            A = line.split(';')
            list1.append(A)
            print(f"service: {list1[0][1]}  price:  {list1[0][2]}")
except FileNotFoundError:
    print("Error: The file does not exist.")
except IOError:
    print("Error: Could not read the file.")
