import random

def calculatePrice(PriceOfLemons,PriceOfCarrots,PriceOfBellpepper):
    TotalPriceofFruit = int(numberOfCarrots) * (PriceOfCarrots) + int(numberOfBellpepper) * (PriceOfBellpepper) + int(
        numberOfLemons) * (PriceOfLemons)
    return TotalPriceofFruit

numberOfLemons = input("Number of Lemons is: ")
numberOfCarrots = input("Number of Carrots is: ")
numberOfBellpepper = input("Number of Bellpepper is: ")

if (int(numberOfBellpepper) > int(numberOfCarrots)):
    print("There are more Bellpeppers thant carrots.")
else:
    print("There are more carrots than bellpeppers")

PriceOfLemons = 0.25
PriceOfCarrots = 0.25
PriceOfBellpepper = 0.5

TotalPriceofFruit = calculatePrice(PriceOfLemons,PriceOfCarrots,PriceOfBellpepper)
TotalPriceofFruit_AtTarget = calculatePrice(.5,.5,.5)

print("Total price at MyStore: ", TotalPriceofFruit)

print("Total price at Target: ", TotalPriceofFruit_AtTarget)