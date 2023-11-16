def NGOs(annual_income, children,):
    if 30000 < annual_income < 40000 and children >= 3:
        subsidy = 1000 * children
        print(subsidy)
        return(subsidy)
    
    elif 20000 < annual_income < 30000 and children >= 2:
        subsidy = 1500 * children
        print(subsidy)
        return(subsidy)

    elif annual_income < 20000:
        subsidy = 2000 * children
        print(subsidy)
        return(subsidy)
