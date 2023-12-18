size = int(input("magic square size : "))
row_no = size
column_no = size

#creating the table and adding the values
list_main = []
list_entries = []
for i in range(1,(row_no*column_no)+1):
    list_entries.append(i)

list_1 = []
while True:
    for i in range(column_no):
        A = int(input("Enter value to add : "))
        if A in range(1,17):
            if A in list_entries:
                list_1.append(A)
                list_entries.remove(A)
                if len(list_1) == column_no:
                    list_main.append(list_1)
                    list_1 = []
                if len(list_entries)==0:
                    break
            else:
                print('value already added')
                print(f'remaining values to add {list_entries}')
        else:
            print(f'value must be in range 1 - {row_no*column_no}')
    if len(list_entries)==0:
        break
for i in list_main:
    print(i)

sums = []
#check for horizontal values
for i in range(row_no):
    sums.append(sum(list_main[i]))
#check for vertical values
for i in range(column_no):
    column_elements = []
    for row in list_main:
        column_elements.append(row[i])
    
    column_sum = sum(column_elements)
    sums.append(column_sum)
#diagonal 1
sum = 0
for i in range(column_no):
    sum += list_main[0+i][0+i]
sums.append(sum)
#diagonal 2
sum = 0
for i in range(column_no):
    sum += list_main[column_no-1-i][0+i]
sums.append(sum)

if len(set(sums))==1:
    print('Its MAGIC !!!')
else:
    print("No magic :(")