month = int(input("Date (month): "))
day = int(input("Date (day): "))

if month % 3 == 0:
    
        if month == 3:
            if day > 21:
                season= "Spring"
            else:
                season= "Winter"
        
        if month == 6:
            if day > 21:
                season= "Summer"
            else:
                season= "Spring"
           
        if month == 9:
            if day > 21:
                season= "Fall"
            else:
                season= "Summer"
            
        if month == 12:
            if day > 21:
                season= "Winter"
            else:
                season= "Fall"
            
else:
    if month < 3:
        season= "Winter"
    if 3 < month < 6:
        season= "Spring"
    if 6 < month < 9:
        season= "Summer"
    if 9 < month < 12:
        season= "Fall"

if month > 12:
    print("Month does not exist")
elif day > 31:
    print("Day does not exist")
else:
    print(season)

