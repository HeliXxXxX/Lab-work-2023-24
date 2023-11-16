#https://github.com/HeliXxXxX
#Bulgarian solitaire 
    #the piles shown as a list with elements "0" so that values getting subtracted and added are more visible

import random as random

def bulgarian_solitaire(number_of_piles, number_of_cards):
    #count of all the active lists (y keeps track of how many lists are made, including empty lists)
    list_active = []
    y = number_of_piles
    for i in range(number_of_piles):
        list_active.append(i)
    #making the new lists
    piles_list = []
    for i in range(0, number_of_piles):
        list_name = f"list_ {i}: "
        new_list = []
        piles_list.append(new_list)
    #the value that will be added to the piles
    x = 0
    #randomly adds values to piles
    n = 0
        #adding 1 value to each list so that starting lists will have atleast one value when starting the game
    for i in range(number_of_piles):
        piles_list[i].append(x)
        #adding the rest of the values randomly
    while n < (number_of_cards-number_of_piles):
        random_number = random.randint(0, number_of_piles - 1)
        piles_list[random_number].append(x)
        n += 1
    #printing the starting piles 
    for i in range(0,number_of_piles):
        print(f"starting pile {i} {piles_list[i]}")
    print(list_active)
    print("")
    #loop for making new piles and adding values to them
    step = 1
    while True:
        #making new list(pile)
        list_name = f"list_ {y}"
        new_list = []
        piles_list.append(new_list)
        #adds a new value to list_active as we made 1 new list
        list_active.append(y)
        #ignoring empty lists to prevent pop from empty list
        for i in list_active:
            if len(piles_list[i]) != 0:
                piles_list[i].pop()
                piles_list[y].append(x)
        #printing the step numbers(each time we make a new pile)
        print("")
        print(f"Step {step}")
        #prints all non empty piles for each step
        for i in range(len(piles_list)):
            if piles_list[i] == []:
                None
            else:
                print(f"pile {i} {piles_list[i]}")
        #checks when to stop the loop
        if len(piles_list[-1]) == 9 and len(piles_list[-2]) == 8 and len(piles_list[-3]) == 7 and len(piles_list[-4]) == 6 and len(piles_list[-5]) == 5 and len(piles_list[-6]) == 4 and len(piles_list[-7]) == 3 and len(piles_list[-8]) == 2 and len(piles_list[-9]) == 1:
            break
        y += 1
        step += 1

if __name__ == "__main__":
    number_of_piles = 5 #any number in range 1-45
    number_of_cards = 45 #code will only work with 45
    bulgarian_solitaire(number_of_piles, number_of_cards)