table = [[" "," "," "],
         [" "," "," "],
         [" "," "," "]]

def print_table():
    for i in range(len(table)):
        print(table[i])

print_table()
def tiktaktoe():
    counter = 0
    if counter%2==0:
        X = input('player X : pick cordinate in format x,y starting from buttom left : ')
        X = X.split(",")
        Xx = int(X[0]) - 1
        Xy = int(X[1]) - 1
        if Xy == 2:
            Xy = 0
        elif Xy == 0:
            Xy = 2
        table[Xy][Xx] = "X"
        print_table()
        counter += 1
    elif counter%2!=0:
        O = input('player O : pick cordinate in format x,y starting from buttom left : ')
        O = O.split(",")
        Ox = int(O[0]) - 1
        Oy = int(O[1]) - 1
        if Oy == 2:
            Oy = 0
        elif Oy == 0:
            Oy = 2
        table[Oy][Ox] = "O"
        print_table()
        counter += 1
running = True
while running:
    tiktaktoe()
    #checks for winning
    #horizontal
    for i in range(len(table)):
        if table[i][0] == table[i][1] == table[i][2]:
            print(f'The winner is {table[i][0]}')
            running = False
            break
    #vertical
    for i in range(3):
        if table[0][i] == table[1][i] == table[2][i]:
            print(f'The winner is {table[0][i]}')
            running = False
    #diagonal
    if table[0][0] == table[1][1] == table[2][2]:
        print(f'The winner is {table[0][i]}')
        running = False
    elif table[0][2] == table[1][1] == table[2][0]:
        print(f'The winner is {table[0][i]}')
        running = False