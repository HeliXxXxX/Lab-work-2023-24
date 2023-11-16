def car_power(velocity):
    p = 1.23
    A = 2.5 
    Cd = 0.2
    power = velocity*(0.5-(p*(velocity**2)*A*Cd))
    Horsepower= power/745.7
    print(f"Power needed = {abs(power)}")
    print(f"Horsepower needed = {abs(Horsepower)}")
    return power, Horsepower

car_power(120)