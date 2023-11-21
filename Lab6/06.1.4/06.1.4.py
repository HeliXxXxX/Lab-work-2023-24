try:
    with open("Lab6\\06.1.4\\input.txt", "r") as file:
        for line in file:
            count = 0
            service = []
            price = []
            for letter in line:
                if letter == ";":
                    count += 1
                if count == 1:
                    service.append(letter)

                elif count == 2:
                    price.append(letter)
                else:
                    None
            service.pop(0)
            price.pop(0)
            print(f"service: {''.join(service)}  price:  {''.join(price)}")


except FileNotFoundError:
    print("Error: The file does not exist.")

except IOError:
    print("Error: Could not read the file.")