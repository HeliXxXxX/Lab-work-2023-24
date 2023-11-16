def bank_balance(years, start_balance, annual_interest):
    new_balance = start_balance
    while years != 0:
        new_balance = new_balance + (annual_interest*new_balance)
        years -= 1
    print(new_balance)
    return(new_balance)

bank_balance(10,1000,0.5)