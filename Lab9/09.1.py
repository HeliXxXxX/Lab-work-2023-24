def neighbor_avarage(values, row, column):
    sum = 0
    attempt = 0
    if row == 0 and column == 0:
        sum += values[row][column+1]
        sum += values[row+1][column]
        sum += values[row+1][column+1]
        return sum/3
    elif row == 0 and column == 1:
        sum += values[row][column-1]
        sum += values[row][column+1]
        sum += values[row+1][column-1]
        sum += values[row+1][column]
        sum += values[row+1][column+1]
        return sum/5
    elif row == 0 and column == 2:
        sum += values[row][column-1]
        sum += values[row+1][column-1]
        sum += values[row+1][column]
        return sum/3
    elif row == 1 and column == 0:
        sum += values[row-1][column]
        sum += values[row-1][column+1]
        sum += values[row][column+1]
        sum += values[row+1][column]
        sum += values[row+1][column+1]
        return sum/5
    elif row == 1 and column == 1:
        sum += values[row-1][column-1]
        sum += values[row-1][column]
        sum += values[row-1][column+1]
        sum += values[row][column-1]
        sum += values[row][column+1]
        sum += values[row+1][column-1]
        sum += values[row+1][column]
        sum += values[row+1][column+1]
        return sum/8
    elif row == 1 and column == 2:
        sum += values[row-1][column]
        sum += values[row-1][column-1]
        sum += values[row][column-1]
        sum += values[row+1][column-1]
        sum += values[row+1][column]
        return sum/5
    elif row == 2 and column == 0:
        sum += values[row-1][column]
        sum += values[row-1][column+1]
        sum += values[row][column+1]
        return sum/3
    elif row == 2 and column == 1:
        sum += values[row][column-1]
        sum += values[row-1][column-1]
        sum += values[row-1][column]
        sum += values[row-1][column+1]
        sum += values[row][column+1]
        return sum/5
    elif row == 2 and column == 2:
        sum += values[row][column-1]
        sum += values[row-1][column-1]
        sum += values[row-1][column]
        return sum/3
        

a = [1,2,3]
b = [4,2,6]
c = [7,8,9]
abc = (a,b,c)
print(neighbor_avarage(abc,0,0))