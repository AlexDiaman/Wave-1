import math

ogbalance = int(input("Please enter the amount you want to diposite: "))

oneyear = ogbalance * 0.04
oneyearbal = ogbalance + oneyear
twoyear = oneyearbal * 0.04
twoyearbal = oneyearbal + twoyear
threeyear = twoyearbal * 0.04
threeyearbal = twoyearbal + threeyear
print("Your balance after 1 year is ", round(oneyearbal,2))
print("Your balance after 2 years is ", round(twoyearbal,2))
print("Your balance after 3 years is ", round(threeyearbal,2))
