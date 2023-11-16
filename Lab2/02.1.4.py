#cost of new car

CostOfCar = 14500

#estimate of the kilometers traveled in a year

DistanceTreavelledPerYear = 30000
DistanceTreavelledPer5Years = DistanceTreavelledPerYear*5

#estimation of the cost of fuel

GasolinePricePerLeter = 2.09

#efficiency in kilometers per liter

KmPerLiter = 15.5
LiterPerKm = 1 / KmPerLiter

#estimate of the resale value of the used car after 5 years

ResalePercentage = 80.36
ResaleValue = CostOfCar*ResalePercentage




PriceForFuel5Years = DistanceTreavelledPer5Years*LiterPerKm*GasolinePricePerLeter

print(PriceForFuel5Years)




